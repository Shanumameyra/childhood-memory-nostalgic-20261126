# NOTES — childhood-memory-nostalgic-20261126

- **Bounty:** Make the AI Judge Feel Nostalgic: A Childhood Memory
- **Slug:** u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363
- **Prize:** $2 total (top 10 paid; 1st $0.62, 2nd $0.43, 3rd $0.30)
- **Deadline:** 21:20 WIB, 26 Nov 2026 (2026-11-26T14:20:00Z)
- **opensAt:** 2026-11-25T08:19:25.000Z (verified via API; before this session started)
- **Fee status:** FREE — entryFeeUsd null (verified via API before building)
- **submissionCount at build time:** 2538
- **Rounds:** blind rounds; final heat at the deadline. Dev board top 500 go on to the final heat (Swiss + playoff of top 12). Judge: z-ai/glm-5.3-flash, pairwise, no ties, margin 1–5.

## Calibration (top-1 standard, from the kit brief — competition is blind, no live board)

Judge criteria, in order:
1. A childhood memory that makes the judge feel nostalgic.
2. Grounded in a concrete place, time or sensation (kitchen, summer evening, smell of fresh rice).
3. Sounds like it truly happened — small honest detail, not greeting-card sentiment.
4. Single clean sentence, ≤280 chars, every word earning its place.
5. Leaves a warm ache that lingers after the sentence ends.

Line chosen (182 chars, one sentence): "When I was seven, my grandmother shelled peas on the porch while the radio crackled, and I still believe the whole world smelled of rain on hot dust and rice steaming in her kitchen."

Why it fits: explicit childhood anchor ("When I was seven"), concrete sensory details (shelling peas, porch, crackling radio, rain on hot dust, steaming rice), honest small detail rather than sentiment, and a lingering warm ache ("I still believe the whole world smelled of..."). Original line, authored from the brief.

## Verification

- `python3 main.py` writes `/output/entry.txt`; output matches `entry.txt` byte-for-byte (verified via a fresh-location run with ENTRY_OUTPUT).
- Entry: 182 characters, UTF-8, single sentence, within the 1–280 gate.
