---
name: wechat-format
version: "1.2.0"
description: >
  将 Markdown 文章转为微信公众号精美排版 HTML。支持 4 套主题（墨石/霓虹黄昏/
  寰宇紫/松烟）、章节卡片、知识盒、立论开篇、高亮框、箭头列表、CSS 表格等 33 种组件。
  Convert Markdown articles to beautifully formatted WeChat-compatible HTML.
  use when user says "排版公众号文章", "wechat format", "微信排版",
  "公众号排版", "format for wechat", "转微信格式"
user-invokable: true
argument-hint: "[markdown-file] [--theme inkstone|neondusk|cosmiclavender|pineink|custom]"
metadata:
  author: ArroyYoung
  tags:
    - wechat
    - formatting
    - publishing
---

# WeChat Article Formatter

LLM-native Markdown-to-WeChat-HTML converter. No external dependencies. Claude reads
Markdown, applies a theme, and generates fully inline-styled HTML ready to paste into
the WeChat Official Account editor.

## References

Before rendering, read these files for detailed specs:

- `references/themes.md` — Four preset themes (Ink Stone, Neon Dusk, Cosmic Lavender, Pine Ink) with full design token JSON. Pick based on article intent: Ink Stone for translations/essays, Neon Dusk for tech product launches, Cosmic Lavender for AI-lab style deep-thought analysis with dramatic serial numbers, Pine Ink for literary tech essays / 8k+ char philosophical longform / "Crossing 十字路口" school of deep commentary.
- `references/components.md` — HTML templates for all components (#1–#20 universal + #21–#28 Cosmic Lavender signature + #29–#33 Pine Ink signature + #34–#36 Cosmic Lavender 2026-05 additions: Knowledge Aside / Core Thesis Box / Reading Card)
- `scripts/cosmic_lavender_reference.py` — working reference implementation of the Cosmic Lavender renderer (parses markdown, applies all 2026-05 rules, writes HTML + preview). Consult when ambiguous about parse order, fence handling, or exact inline style strings. Not authoritative on visual spec — `themes.md` + `components.md` are. But canonical for parsing/output behavior.
- `references/wechat-constraints.md` — WeChat rendering constraints and safe CSS properties

## Design Principles

1. **All CSS inline** — Every element carries its own `style=""`. No `<style>` tags, no classes.
2. **Section-only structure** — Use `<section>` for all structural elements. Never `<div>`.
3. **No banned elements** — Never use native `<ul>/<ol>/<li>`, `<table>/<tr>/<td>`, or `<blockquote>`.
4. **No JS, no pseudo-elements** — No `<script>`, no `::before`/`::after`.
5. **Dark mode safe** — Never hardcode `#fff` or `white` backgrounds. Use `rgba()` with low opacity.
6. **External links become footnotes** — Only `mp.weixin.qq.com` links stay clickable.
7. **CJK-first typography** — Dual font system: serif headings + sans-serif body, 1.9 line height.

---

## Phase 1: READ

1. Read the Markdown file provided by the user.
2. Parse YAML frontmatter (if present) to extract metadata:

```yaml
---
title: 文章标题               # Required — article title
author: Arron                 # Optional — for Author Card
account: 公众号名称            # Optional — for Author Card
theme: inkstone               # inkstone (default) | neondusk | /path/to/custom.json
source: FROM ANTHROPIC        # Optional — triggers Source Block
source_note: 本文翻译自...    # Optional — source description
source_url: https://...       # Optional — original link
---
```

3. Load the theme from `references/themes.md`. Theme names: `inkstone` (default), `neondusk`, `cosmiclavender`, `pineink`. If `theme` is a file path, read the custom JSON.
4. If no frontmatter, use all defaults (theme: inkstone, no source block, no author card).
5. If theme is `cosmiclavender`, also load the Cosmic Lavender signature components (#21–#28 in `components.md`) and apply the overrides in the Cosmic Lavender Assembly Cheat Sheet.
6. If theme is `pineink`, also load the Pine Ink signature components (#29–#33 in `components.md`) and apply the overrides in the Pine Ink Assembly Cheat Sheet.

---

## Phase 2: ANALYZE

### Detect Article Structure Mode

| Mode | Condition | Behavior |
|------|-----------|----------|
| **A: Long-form + Chapters** | Has `:::chapter` fences | Chapter Cards + auto TOC + dividers between chapters |
| **B: Standard Article** | Has H2/H3 but no `:::chapter` | H2/H3 as visual nodes, no TOC unless explicit `:::toc` |
| **C: Short Post** | No H2/H3 | Flat paragraph layout, no Source/Author unless explicit |

### Build Document Outline

- Collect all H2/H3 headings (for potential TOC).
- Count `:::chapter` fences and assign palette colors by index (cycling through `chapterPalette`).
- Collect all `[text](url)` links where URL is NOT `mp.weixin.qq.com` — these become footnotes.
- Estimate reading time: `ceil(chinese_char_count / 300)` minutes.

---

## Phase 3: RENDER

Convert each Markdown element to its HTML component using templates from `references/components.md`.
Apply the active theme's design tokens (colors, fonts, spacing) to every inline style.

### Markdown-to-Component Mapping

| Markdown Syntax | Component | Notes |
|-----------------|-----------|-------|
| `# H1` | Article title (one per article, in Source Block or standalone) | |
| `## Heading` | Section Heading H2 — primary color, serif | |
| `### Heading` | Subsection Heading H3 — serif, primary color span | |
| `paragraph text` | Body Paragraph | |
| `**bold**` | Bold Emphasis — `font-weight:600`, heading color | |
| `***accent***` | Accent Emphasis — primary color + bold | |
| `` `code` `` | Inline Code — monospace, tinted background | |
| ` ```lang ``` ` | Code Block — pre/code in rounded container | |
| `> quote` | Callout Box — left border accent | |
| `- item` | Bullet List — `●` prefix in section/p | |
| `1. item` | Numbered List — zero-padded `01` prefix | |
| `\| table \|` | CSS Table — `display:table` / `display:table-cell` | |
| `---` | Divider — thin border-top line | |
| `![alt](src)` | Image — rounded, centered, optional caption from alt | |
| `[text](url)` | External link → footnote `[N]` superscript (auto-collected) | mp.weixin.qq.com exempt |

### Custom :::fence Extensions

```
:::source             — Source Block (translation credit, origin link)
:::chapter            — Chapter Card (colored, with label + title + subtitle)
:::toc                — Table of Contents (auto-generated from headings)
:::callout / :::tip   — Callout Box (left border, primary color)
:::warning            — Callout Box variant (amber border)
:::success            — Callout Box variant (green border)
:::exercise           — Callout Box (same as callout, for exercises)
:::highlight          — Highlight Box (tinted background, centered text)
:::important          — Highlight Box (alias)
:::steps              — Arrow List (→ prefix items with bold title)
:::author             — Author Card (name, account, bio)
:::lead               — Vertical Rail Lead Paragraph (Cosmic Lavender — purple 6×75 left bar)
:::quote              — Asymmetric Quote Box (Cosmic Lavender — purple left rail + slate sides)
:::softbreak          — Cream Hairline Divider (Cosmic Lavender — warm 1px line)
:::label TEXT         — Purple Pill + Rule, optional label (Cosmic Lavender — micro section opener)
:::thesis             — Inline thesis-sentence highlight (Cosmic Lavender — purple 20% wash)
:::byline             — Optima Author Byline at top of article (Cosmic Lavender / Pine Ink)
:::section NN         — Force a numbered section mark with serial NN (Cosmic Lavender)
:::aside              — Knowledge Aside / "你知道吗" box (Pine Ink — green-bordered mint-mist box; Cosmic Lavender — #34 purple-bordered lavender-tinted box; first non-empty line = purple/green bold title; multi-paragraph body supported via blank lines; per-line breaks via `<br/>`)
:::manifesto          — Pine Manifesto Opener (Pine Ink — gray bg + green left rail thesis block, max once per article)
:::pine-chapter       — Force a Pine Chapter Heading explicitly (Pine Ink)
:::reading TITLE      — Reading Recommendations (Cosmic Lavender #36 — card stack with cover image + title + lavender chevron; each card = 3 consecutive lines: image-url / title / article-url; blank line separates cards; optional TITLE renders Purple Pill + Rule header above stack)
```

**Fence format:**

```markdown
:::type
content lines...
:::
```

### Smart Features (apply during rendering)

1. **CJK-Latin auto-spacing** — Insert a space between CJK characters and Latin/numbers.
   `AI时代` becomes `AI 时代`, `Claude的API` becomes `Claude 的 API`.

2. **Smart punctuation** — In Chinese-context text:
   - `"..."` → `「...」`
   - `(...)` → `（...）`
   - Normalize ellipsis sequences.

3. **Auto footnotes** — Scan all `[text](url)` links:
   - If URL contains `mp.weixin.qq.com` → keep as `<a>` tag.
   - Otherwise → replace with `text<sup>[N]</sup>` and collect URL for footnote section.

4. **Chapter color rotation** — Chapter Cards cycle through `chapterPalette`:
   Chapter 1 → `palette[0]`, Chapter 2 → `palette[1]`, ... wrapping at array length.

5. **Reading time** — Calculate `ceil(total_chinese_chars / 300)` and display as a caption
   line near the top: `约 X 分钟阅读`.

6. **Cosmic Lavender auto-applies** (when active theme is `cosmiclavender`):
   - Auto-number all `## H2` headings as `01.`, `02.`, ... rendered with #21 Numbered Section Mark
   - Skip numbering for: `## TL;DR`, `## 目录`, `## 参考链接`, `## 关于作者`, `## 写在最后`, `## 先说结论`. If H2 starts with `结语` or `结语：`, render with #26 Purple Pill + Rule using label "EPILOGUE" instead of a number.
   - Wrap the FIRST sentence of the FIRST paragraph after each `## H2` with #23 Thesis-Sentence Highlight (skip if that paragraph is entirely bold — see Core Thesis Box rule below)
   - Use #25 Cream Hairline Divider for all `---` (not the standard charcoal rule)
   - **DO NOT** auto-emit a divider before each `## H2`. The markdown's explicit `---` between sections is the source of truth — auto-emitting a second divider stacks visible double lines. Trust the markdown.
   - **`**整段全粗**` (whole-paragraph bold)** → auto-renders as #35 Cosmic Lavender Core Thesis Box (rounded lavender container, bold body in BLACK #000; matches #34 aside visually, sans the title row).
   - **Inline `**bold**` in body** → renders in theme PURPLE `#7973F7` (low-cost highlighter). Exceptions: bold inside any already-lavender container (#34 aside body, #35 thesis box, #24 quote box) stays BLACK `#000` to preserve hierarchy.
   - **`## H2` body padding** = `0 8px` (tightened from 16px in 2026-05 for long-form readability — gains ~4 CJK chars per line on 375px screens). Box-internal padding (asides, callouts) stays at the original `14-16px / 16-22px` so internal content still feels "set in".
   - **`### H3` size** = `17px` (tightened from 20-22px in 2026-05 for clearer H2/H3 subordination). Margin = `24px auto 12px`, line-height = `1.6`.
   - **`### H3` with `:::label X` pill** (e.g. L0–L5 layer headers, company subsections) → renders as **single-row inline pattern**: `[6px×20px purple pill] [optional Optima label] [17px title]`. NO trailing horizontal rule. The old two-row "pill+rule / title-below" pattern produces a "broken divider" visual when no label fills the gap.
   - **`:::aside`** → renders #34 Cosmic Lavender Knowledge Aside (purple-bordered, `#FAF8FF` background, 8px radius, 14px/16px padding). First non-empty line = purple bold title; remaining lines = body. Multi-paragraph supported: each markdown line becomes a rendered line separated by `<br/>`; blank lines add `<br/><br/>` paragraph spacing. No max-line cap (long asides are first-class).
   - **`:::reading`** → renders #36 Cosmic Lavender Reading Card stack. See fence spec above.
   - **`---` (cream divider) preceding H2** — render normally; the H2 itself adds no extra divider.
   - Body font = `PingFangSC-light`, line-height = `2`, paragraphs separated by blank `<p><br></p>` not margin-bottom
   - All H1/H2/H3 use PingFang **Light** (font-weight: 300 or absent + `<strong>` for bold) — hierarchy by SIZE not by weight

7. **Pine Ink auto-applies** (when active theme is `pineink`):
   - Render ALL `## H2` headings as #29 Pine Chapter Heading (centered, 24px sage `#407600` bold, 8px green underline, `width:fit-content`, `margin:80px auto 40px auto`). First chapter in the article: reduce top margin to `40px`.
   - Render all `### H3` as 17px sage `#407600` bold (NOT centered, NO underline) with `margin:40px 0 16px` — keeps the underline mark exclusive to chapter-level
   - If the FIRST `> blockquote` appears BEFORE the first `## H2`, render it as #30 Pine Manifesto Opener (auto-elevation). Subsequent `> blockquote` render as standard #11 Callout with sage colors (border-left `3px solid #407600`, bg `#F5F5F5`).
   - `:::aside` blocks → #31 Knowledge Aside (first non-empty line becomes green bold title; remaining lines = body; separate body paragraphs with inline `<br/><br/>`, NOT separate `<p>` blocks)
   - `:::byline` → #32 Pine Author Byline (right-aligned, single Optima/PingFang stack, padding-bottom 1em)
   - Footnotes → #33 Pine Footnote (three-tier gray: `#222` index, `#555` label, `#888` URL, 12px / 1.7)
   - **`letter-spacing: 0.1em` on EVERY text element.** Body, headings, captions, code, footnotes, asides — without exception. Only `<sup>` footnote markers use `letter-spacing:0` (keeps `[1]` tight).
   - Body font stack = single shared `Optima → PingFang Light → serif fallback` (no separate heading font, no serif/sans split)
   - Body line-height = `26px` literal (NOT `1.75` relative) inside boxes/blocks; `1.75` is fine on the outer wrapper
   - Paragraphs separated by real `margin: 20px 0`, NOT blank `<p><br></p>` (opposite of Cosmic Lavender)
   - Text-align = `left` everywhere (NOT `justify` — reads more like a printed manuscript)
   - `**bold**` color = `#222222` (NOT sage — sage is reserved for headings, `***accent***`, manifesto opener, aside titles only)
   - `***accent***` color = `#407600` (sage)
   - Image `border-radius` = `10px` (NOT default 6px)
   - DO NOT auto-emit: TOC, numbered serial marks, first-sentence marker highlights, chapter color rotation
   - `:::chapter` fence is downgraded to #29 Pine Chapter Heading (uses the chapter's main title text only — Pine Ink doesn't have colored chapter cards)

---

## Phase 4: ASSEMBLE

### Content Wrapper Structure

Wrap the entire article in a single outer section:

```html
<section style="background:{pageBg};padding:0;">
  <!-- 1. Source Block (if frontmatter has source) -->
  <!-- 2. Chapter Card (if Mode A, for each chapter) -->
  <!-- 3. Content sections, each wrapped: -->
  <section style="max-width:{maxWidth};margin:0 auto;padding:{contentPadding} {contentPadding};">
    <!-- paragraphs, headings, inline components -->
  </section>
  <!-- 4. Dividers between major sections -->
  <!-- 5. Footnote section (if any external links) -->
  <!-- 6. Author Card (if frontmatter has author+account) -->
</section>
```

### Assembly Rules

- **Mode A:** Insert Chapter Card before each chapter's content. Auto-generate TOC after
  Source Block (or at article start). Insert divider between chapters.
- **Mode B:** Flow content naturally with H2/H3 as section breaks. TOC only if explicit `:::toc`.
- **Mode C:** Flat flow. No structural decorations unless explicitly fenced.
- **Always:** Add footnote section at the end if any external links were collected.
- **Always:** Add Author Card at the very end if `author` + `account` are in frontmatter.

---

## Phase 5: OUTPUT

### Step 1: Save Article HTML

Save the pure article HTML (for pasting) to a file next to the source Markdown:

```
{source_dir}/{filename}-wechat.html
```

If the source is `/path/to/article.md`, output to `/path/to/article-wechat.html`.

### Step 2: Generate Preview Page

Read the preview template from `scripts/copy-to-clipboard.html`. Inject the article HTML
into the template's `#article-content` container. Save the preview page:

```
/tmp/wechat-article-preview.html
```

If the template at `scripts/copy-to-clipboard.html` does not exist, generate a self-contained
preview page with:
- A sticky toolbar with title and "复制文章" button
- A 375px phone-frame preview container
- Character count and reading time stats
- Clipboard API copy (HTML + plain text) with fallback to `execCommand('copy')`

### Step 3: Open Preview

```bash
open /tmp/wechat-article-preview.html
```

### Step 4: Report to User

Print a summary:
- Article title
- Theme used
- Structure mode (A/B/C)
- Character count and reading time
- Number of footnotes generated
- Output file paths
- Instruction: "Click '复制文章' in the preview, then paste into mp.weixin.qq.com editor."

---

## WeChat Constraints Checklist

Before outputting, verify ALL 16 items pass:

- [ ] All CSS is inline `style=""` — no `<style>` tags, no class dependencies
- [ ] No `<script>` tags
- [ ] No `position: fixed` or `position: absolute`
- [ ] No CSS variables `var(--xxx)`
- [ ] No `calc()` expressions
- [ ] No `@media` queries
- [ ] No `@font-face`
- [ ] No `@keyframes` / CSS animations
- [ ] No `::before` / `::after` pseudo-elements
- [ ] Lists use section/p with span prefixes — no native `<ul>/<ol>/<li>`
- [ ] Tables use `display:table`/`display:table-cell` — no native `<table>/<tr>/<td>`
- [ ] Quotes use section with border-left — no native `<blockquote>`
- [ ] All external links converted to footnotes (except mp.weixin.qq.com)
- [ ] Image dimensions set via `style` not HTML attributes
- [ ] All structural elements are `<section>` not `<div>`
- [ ] All text elements include `word-break:break-all`

If any item fails, fix it before saving.

---

## Dark Mode Safety

WeChat dark mode inverts/adjusts certain colors. Follow these rules:

- **NEVER** use `background:#fff`, `background:white`, or `background:#ffffff`
- **USE** `rgba()` low-opacity backgrounds: e.g. `rgba(26,26,24,0.02)` — nearly invisible in dark mode
- **NEVER** use very light gray text (invisible when dark mode inverts)
- **USE** medium gray body text like `#4a4a45` — inverts to readable light color in dark mode
- **Chapter Cards** use vibrant but not extreme colors (Sunset Sweep E+ palette) that remain recognizable after inversion
- **Highlight boxes** use `rgba(primary, 0.06)` — subtle in both modes
- **Dividers** use `rgba()` with 0.15-0.18 opacity — visible in both modes

---

## Error Handling

- **No frontmatter:** Use defaults (inkstone theme, no source/author blocks).
- **Unknown theme name:** Warn user, fall back to inkstone.
- **No Markdown file argument:** Ask user for the file path.
- **Empty or very short content:** Render as Mode C (short post).
- **Image URLs:** Warn user that external image URLs may not survive WeChat CDN requirements.
  Include the images in output but add a note about uploading to WeChat.
- **Content over 20,000 chars:** Warn user about WeChat's content size limit.
