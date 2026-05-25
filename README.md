# wechat-format

Claude Code skill for formatting Markdown into beautifully styled WeChat Official Account articles.

Write in Markdown, get magazine-quality WeChat HTML. No dependencies, no scripts, no build step.

## Install

```bash
git clone https://github.com/ArroyYoung/wechat-format.git ~/.claude/skills/wechat-format
```

Or one-liner:
```bash
curl -fsSL https://raw.githubusercontent.com/ArroyYoung/wechat-format/main/install.sh | bash
```

## Usage

In Claude Code:

```
/wechat-format article.md
/wechat-format article.md --theme neondusk
/wechat-format article.md --theme cosmiclavender
/wechat-format article.md --theme pineink
```

This will:
1. Convert your Markdown to WeChat-compatible HTML (all inline CSS, no JS)
2. Open a 375px phone-frame preview in your browser
3. Click "Copy" button, paste into mp.weixin.qq.com editor, done

## Themes

### Ink Stone (Default)

Warm editorial palette. Burnt sienna accents, serif headings, 1.9 line-height.
Chapter cards use a Sunset Sweep gradient: Indigo -> Violet -> Rose -> Orange -> Amber.

### Neon Dusk

Cool tech-editorial palette. Deep indigo primary, coral accents.
Chapter cards follow a sunset gradient from twilight to amber glow.

### Cosmic Lavender (寰宇紫)

Deep-thought editorial palette inspired by AI lab / VC research publications
(海外独角兽, Stratechery, Anthropic blog). Signature lavender `#7973F7` accent
on a neutral warm cream base. Built around **PingFang Light** typography at
**line-height 2.0** — the airy, reads-like-a-book feel that signals "this is
a serious cognitive piece." Includes 8 signature components: numbered section
mark (giant 55px purple serial), vertical rail lead, thesis-sentence highlight,
asymmetric quote box, cream hairline divider, purple pill+rule, lavender disc
bullet, and Optima byline. Best for: company teardowns, science explainers,
brand longform, AI research commentary.

### Pine Ink (松烟)

Literary deep-read editorial palette inspired by the "Crossing 十字路口" school of
considered tech commentary. Single sage-green `#407600` accent (the color of
pine-soot ink stick) on warm gray. Built around **0.1em letter-spacing on every
element** — the slow, deliberate breathing room that signals "this is meant to be
lingered over." Pairs Optima Latin with PingFang Light Chinese in a single shared
stack — no separate heading font. Includes 5 signature components: pine chapter
heading (8px sage underline with 80px breathing room), pine manifesto opener
(gray bg + green left rail thesis), knowledge aside ("你知道吗" mint-mist box),
pine author byline, pine footnote. Best for: literary tech essays, philosophical
product analysis, multi-chapter deep-reads (8k+ chars), founder-letter longform,
considered translations. Sister theme to Cosmic Lavender — same "serious cognitive
piece" register, opposite aesthetic.

### Custom

Copy any theme JSON from `references/themes.md`, modify colors, save as `.json`, use with `--theme /path/to/theme.json`.

## Components (36)

### Universal (1–20)

| Component | Markdown Trigger |
|-----------|-----------------|
| Source Block | `:::source` |
| Chapter Card | `:::chapter` |
| Table of Contents | `:::toc` |
| Section Heading | `## heading` |
| Subsection Heading | `### heading` |
| Body Paragraph | plain text |
| Bold | `**bold**` |
| Accent (primary color) | `***accent***` |
| Inline Code | `` `code` `` |
| Code Block | ` ```lang ``` ` |
| Callout / Tip | `> quote` or `:::callout` |
| Warning | `:::warning` |
| Highlight Box | `:::highlight` |
| Arrow List | `:::steps` |
| Numbered List | `1. item` |
| Bullet List | `- item` |
| CSS Table | `\| a \| b \|` |
| Divider | `---` |
| Image | `![alt](src)` |
| Author Card | `:::author` |

### Pine Ink signatures (29–33)

These activate automatically when `theme: pineink`, or via explicit fences:

| Component | Markdown Trigger |
|-----------|-----------------|
| Pine Chapter Heading (sage + 8px underline + 80px breathing) | `## heading` → centered green title |
| Pine Manifesto Opener (gray bg + green left rail thesis) | First `> blockquote` before `## H2`, or `:::manifesto` |
| Knowledge Aside / "你知道吗" Box | `:::aside` (first line = green bold title) |
| Pine Author Byline (right-aligned, single Optima stack) | `:::byline` |
| Pine Footnote (three-tier gray editorial) | auto |

### Cosmic Lavender signatures (21–28, 34–36)

These activate automatically when `theme: cosmiclavender`, or via explicit fences:

| Component | Markdown Trigger |
|-----------|-----------------|
| Numbered Section Mark (55px purple serial) | `## heading` → auto `01.` `02.` ... |
| Vertical Rail Lead | `:::lead` |
| Thesis-Sentence Highlight | first sentence after `## H2`, or `:::thesis` |
| Asymmetric Quote Box (purple left rail + slate 3 sides) | `> quote` or `:::quote` |
| Cream Hairline Divider | `---` (overrides default) |
| Purple Pill + Rule (incl. **H3 inline pill** variant) | `:::label TEXT` / `### H3` w/ pill |
| Lavender Disc Bullet | `- item` (overrides default) |
| Optima Author Byline | `:::byline` |
| **Knowledge Aside** ("你知道吗" 紫框淡紫底, multi-paragraph) | `:::aside` |
| **Core Thesis Box** (rounded lavender container, black bold body) | `**整段全粗**` (whole-paragraph bold) |
| **Reading Card** (WeChat-style image + title + chevron stack) | `:::reading TITLE` |

**Inline bold color rule** — `**xxx**` in body text renders in theme purple `#7973F7`; inside any lavender container (#34 aside body, #35 thesis box, #24 quote box), bold stays black `#000` to preserve hierarchy.

External links are auto-converted to footnotes (WeChat blocks non-WeChat URLs).

## Smart Features

- **CJK-Latin spacing** - auto inserts spaces between Chinese and English
- **Smart punctuation** - normalizes quotes and brackets for Chinese context
- **Auto footnotes** - external links become numbered references
- **Chapter color rotation** - cycles through the theme's sunset palette
- **Reading time** - estimated from character count

## Frontmatter (Optional)

```yaml
---
title: Article Title
author: Your Name
account: Your WeChat Account
theme: inkstone
source: FROM SOURCE
source_note: Translated from...
source_url: https://...
---
```

## Article Modes

The skill auto-detects your article structure:

| Mode | Condition | Result |
|------|-----------|--------|
| A: Long-form | Has `:::chapter` | Chapter cards + auto TOC + dividers |
| B: Standard | Has `##` headings | Headings as visual anchors |
| C: Short | No headings | Clean paragraph flow |

## WeChat Constraints Handled

All output is WeChat-safe:
- Inline CSS only (no `<style>` tags)
- `<section>` structure (no `<div>`)
- No `<ul>/<ol>`, `<table>`, `<blockquote>` (WeChat breaks them)
- No JS, no CSS variables, no animations
- Dark mode safe (rgba backgrounds, no hardcoded white)
- External links auto-converted to footnotes

## File Structure

```
wechat-format/
  SKILL.md                    # Core skill instructions
  references/
    themes.md                 # Theme definitions
    components.md             # 20 component HTML templates
    wechat-constraints.md     # WeChat rendering rules
  scripts/
    copy-to-clipboard.html    # Preview page template
  examples/
    demo-chapters.md          # Example article with chapters
  install.sh                  # One-liner installer
  LICENSE                     # MIT
```

## License

MIT
