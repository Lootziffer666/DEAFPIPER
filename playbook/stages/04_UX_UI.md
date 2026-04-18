# 04_UX_UI – UX/UI, Flows & UX-Writing

## Ziel

Du machst das Produkt für Menschen benutzbar: Flows, Sprache, Struktur, minimaler Design-Rahmen.

## Inputs

- PRD.json
- Zielgruppe/Tone
- Constraints (Accessibility, Plattform)

## Outputs (am Ende dieses Schritts)

- UX_SPEC.json
- Wireframes/Proto (optional)
- copy.md
- design_tokens.md

## Vorgehen (pragmatisch)

1. Skizziere 1–3 Kern-Journeys (Happy Path + Edge Cases).
2. Leite daraus Screens/IA ab (Sitemap/Navigation).
3. Schreibe Microcopy dort, wo Nutzer hängen bleiben (Errors, Empty States, CTAs).
4. Definiere Tokens/Komponenten, die du wirklich brauchst (nicht 200).

## Quality Gates

- Der Hauptflow ist in < 60 Sekunden erklärbar.
- Accessibility: Kontraste, Fokus, Tastatur, klare Sprache berücksichtigt.

## Short-Prompt (copy/paste)

```txt
Du bist mein UX-Lead. Basierend auf PRD.json erzeuge:
1) User Journeys + Hauptflows,
2) IA/Sitemap,
3) UX Writing (Tonality + Microcopy),
4) Design-System-Starter (Tokens + Kernkomponenten).

Input:
{PRD_JSON}

Output:
- UX_SPEC.json
- copy.md (Microcopy-Tabelle)
- design_tokens.md
```

## Templates

- `/templates/UX_SPEC.json`

## GPT-Config

- `/gpt_configs/04_UX_UI.json`

## Toolbox-Vertiefung

- `/toolbox/04__UX_UI_DESIGN.md`
- `/toolbox/P08_BRAND_AND_VISUAL_DESIGN.md`
- `/toolbox/P12_REWRITE_AND_TONE.md`

## Toolbox (SSOT)
- `toolbox/P08_BRAND_AND_VISUAL_DESIGN.md` (Mini Brand Kit + Logo Workflow)
- `toolbox/P12_REWRITE_AND_TONE.md`
