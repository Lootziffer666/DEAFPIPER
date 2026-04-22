from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Mapping

from .agent_instruction import AgentInstructionSet
from .audit import AuditLogger


@dataclass(frozen=True)
class ProviderBinding:
    provider_id: str
    model_id: str
    endpoint_ref: str
    cost_profile: Dict[str, float]
    capabilities: Dict[str, Any]


class ModelCapabilityRegistry:
    def __init__(self) -> None:
        self._capabilities: Dict[str, Dict[str, Any]] = {}

    def register(self, model_id: str, capabilities: Mapping[str, Any]) -> None:
        self._capabilities[model_id] = dict(capabilities)

    def query(self, model_id: str) -> Dict[str, Any]:
        if model_id not in self._capabilities:
            raise KeyError(f"Unknown model_id: {model_id}")
        return dict(self._capabilities[model_id])


class ProviderResolver:
    def __init__(self, capability_registry: ModelCapabilityRegistry) -> None:
        self.capability_registry = capability_registry

    def resolve(self, instruction_set: AgentInstructionSet, policy: Mapping[str, Any]) -> ProviderBinding:
        default_model = policy.get("default_model", "model-default")
        provider_id = policy.get("provider_id", "local")
        endpoint_ref = policy.get("endpoint_ref", "local://runtime")
        capabilities = self.capability_registry.query(default_model)

        return ProviderBinding(
            provider_id=provider_id,
            model_id=default_model,
            endpoint_ref=endpoint_ref,
            cost_profile={"in_per_million": float(policy.get("in_per_million", 0.0)), "out_per_million": float(policy.get("out_per_million", 0.0))},
            capabilities=capabilities,
        )


class CostAccountant:
    def __init__(self) -> None:
        self._records: Dict[str, List[Dict[str, Any]]] = {}

    def record(self, execution_ref: str, tokens: int, duration: float, provider_binding: ProviderBinding) -> None:
        self._records.setdefault(execution_ref, []).append(
            {
                "tokens": tokens,
                "duration": duration,
                "provider_id": provider_binding.provider_id,
                "model_id": provider_binding.model_id,
                "cost_profile": provider_binding.cost_profile,
            }
        )

    def summarize(self, task_ref: str) -> Dict[str, Any]:
        records = self._records.get(task_ref, [])
        return {
            "task_ref": task_ref,
            "executions": len(records),
            "tokens": sum(r["tokens"] for r in records),
            "duration": sum(r["duration"] for r in records),
        }


class ToolBroker:
    def __init__(self, audit_logger: AuditLogger | None = None) -> None:
        self.audit_logger = audit_logger

    def invoke(self, tool_id: str, params: Mapping[str, Any], instruction_set: AgentInstructionSet) -> Dict[str, Any]:
        allowed = {tool.tool_id: tool.scope for tool in instruction_set.allowed_tools}
        if tool_id not in allowed:
            result = {"status": "denied", "error": "tool not in allow-list"}
        else:
            result = {"status": "ok", "tool_id": tool_id, "params": dict(params), "scope": allowed[tool_id]}

        if self.audit_logger:
            self.audit_logger.log(
                actor={"type": "agent", "id": "tool_broker"},
                subject_type="Task",
                subject_id=instruction_set.task_ref,
                event="tool_called",
                previous_state=None,
                new_state=None,
                payload={"tool_id": tool_id, "params": dict(params), "result": result},
            )

        return result
