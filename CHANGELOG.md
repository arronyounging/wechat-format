# Changelog

## v1.2.0 — 2026-05-25 · Cosmic Lavender long-form polish

This release focuses on making Cosmic Lavender comfortable for 10k+ character
articles. Adds three new signature components (#34–#36), reworks the H3 inline
pattern, tunes spacing for long-form readability, and codifies a bold-color
hierarchy that keeps the theme's purple "spent meaningfully" rather than
splashed everywhere.

### Added

- **#34 Cosmic Lavender Knowledge Aside (`:::aside`)** — purple-bordered
  `#FAF8FF`-tinted box for "你知道吗" sidebar definitions, thought experiments,
  and background context. Multi-paragraph body via blank lines; per-line breaks
  via direct markdown line breaks; no maximum line cap. Inline `**bold**`
  inside aside body stays black to preserve hierarchy against the purple title.
- **#35 Cosmic Lavender Core Thesis Box** — auto-emitted when a whole markdown
  paragraph is wrapped in `**...**`. Same rounded lavender container as #34
  without the title row — the bold body itself is the punchline. Replaces the
  old flat `rgba(163,140,239,0.18)` highlight box (which looked "out of family"
  after the rest of the theme moved to rounded lavender containers).
- **#36 Cosmic Lavender Reading Card (`:::reading TITLE`)** — WeChat-native
  图文卡片 style: stacked cards with full-width banner + single-line title +
  circular lavender chevron. Each card = 3 lines (image / title / url),
  blank-line separated. Includes three layers of margin suppression to defeat
  WeChat editor's auto-`<p>`-wrap of `<img>` (the bug that produced ~90px
  ghost gaps between image and title row).
- **Inline pill H3 variant** documented under #26 — for `### H3` carrying a
  pill marker (L0–L5 layer headers, company subsections in comparisons), render
  as a single flex row of `[pill][optional label][title]` with NO trailing
  rule. Replaces the old two-row "pill+rule / title-below" pattern, which
  looked like a broken divider whenever the label-between-pill-and-rule was
  empty.
- **`scripts/cosmic_lavender_reference.py`** — working reference renderer
  capturing all v1.2.0 parsing rules. Not authoritative on visual spec, but
  canonical for parse-order and output-byte behavior.
- **`CHANGELOG.md`** + **`.gitignore`** — first cut.

### Changed

- **Cosmic Lavender `contentPadding`** tightened from `16px` → `8px`. The
  16px default felt cramped on 375px-wide phone screens (~22 CJK chars per
  line); 8px gains ~4 chars per line without losing breathing room. Box-internal
  padding (`calloutPadding`, `highlightPadding`) stays at `16-22px` so highlight
  blocks still feel "set in" against the wider body.
- **Cosmic Lavender `h3Size`** tightened from `20px` → `17px`. The 20-22px H3
  was too close to the 30px H2 title, magnifying the H2/H3 ratio to 1.36 —
  H3 felt like a second H2. New 17px makes the ratio 1.76, matching Pine Ink
  and Stratechery/海外独角兽 conventions.
- **Inline `**bold**` color rule** added — body bold renders in theme purple
  `#7973F7` (low-cost highlighter that pulls the eye); bold inside any
  already-lavender container (#34 aside body, #35 thesis box, #24 quote box)
  stays black `#000` to preserve hierarchy. Codifies the principle that purple
  is for "emphasis in white space," black is for "emphasis inside a purple
  container."
- **#24 Asymmetric Quote Box** spacing aligned with #34/#35: `border-radius:8px`,
  `padding:14px 16px`, `margin:20px auto`. The purple left rail naturally
  curves into a small "leaf" at its corners — intended look.
- **`## H2` divider behavior** — Cosmic Lavender no longer auto-emits a cream
  hairline before each H2. The markdown's explicit `---` between sections is
  the source of truth. Auto-emitting a second divider was stacking visible
  double lines on every section break.
- **`## 结语` H2** now renders with the #26 Purple Pill + Rule using label
  `EPILOGUE` instead of a section number.
- **`## 先说结论`** added to the no-number skip list (alongside `## TL;DR`,
  `## 目录`, `## 参考链接`, `## 关于作者`, `## 写在最后`).

### Fixed

- WeChat editor's `<img>` auto-`<p>`-wrap inserting a ~90px gap below banner
  images inside the Reading Card. Now defended with `font-size:0` on the card
  + image wrapper, `vertical-align:bottom` on the `<img>` itself, and explicit
  `margin:0` resets throughout.

### Migration notes

No breaking markdown changes. All existing articles render with tighter spacing
and the new bold-color rule. If you specifically want the old behavior:

- For 16px body padding, override `theme.spacing.contentPadding` in a custom
  theme JSON.
- For black inline bold (Pine Ink-style), wrap your `**bold**` in a fenced
  container like `:::quote` or `:::aside` — bold inside any lavender container
  remains black by spec.

---

## v1.1.0 — Cosmic Lavender release

- Add Cosmic Lavender theme + 8 signature components (#21–#28).

## v1.0.0 — Initial release

- Ink Stone (default) and Neon Dusk themes.
- 20 universal components.
- WeChat-safe inline-style rendering.
