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

### Custom

Copy any theme JSON from `references/themes.md`, modify colors, save as `.json`, use with `--theme /path/to/theme.json`.

## Components (20)

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
