# WeChat Format Themes

## Theme: Ink Stone (墨石) — Default

Refined editorial palette inspired by Chinese mineral pigments and Japanese wabi-sabi.
Warm analogous base (red-orange through yellow-brown) with split-complementary
extension into blue-green. Every color has a red-brown undertone that ties the system
together. Evokes: Monocle magazine, handmade Xuan paper, sumi ink, Aesop interiors.

```json
{
  "name": "墨石 Ink Stone",
  "colors": {
    "primary": "#B8553A",
    "primaryLight": "rgba(184,85,58,0.06)",
    "primaryBorder": "rgba(184,85,58,0.2)",
    "text": "#4A3F3A",
    "heading": "#2C2420",
    "bold": "#2C2420",
    "caption": "#7A6D66",
    "link": "#8E5E3E",
    "codeText": "#6B5044",
    "codeBg": "rgba(107,80,68,0.06)",
    "divider": "rgba(44,36,32,0.15)",
    "cardBorder": "rgba(44,36,32,0.08)",
    "pageBg": "rgba(44,36,32,0.03)",
    "surfaceHighlight": "rgba(184,85,58,0.06)",
    "calloutWarning": "#9C6226",
    "calloutWarningBg": "rgba(156,98,38,0.08)",
    "calloutSuccess": "#4D7A5C",
    "calloutSuccessBg": "rgba(77,122,92,0.08)",
    "chapterPalette": ["#4F46E5", "#9333EA", "#DB2777", "#EA580C", "#CA8A04"],
    "chapterNames": ["Indigo 靛蓝", "Violet 紫", "Rose 玫红", "Orange 橙", "Amber 琥珀"]
  },
  "typography": {
    "body": "'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif",
    "heading": "'Noto Serif SC','Songti SC',STSong,Georgia,serif",
    "code": "'JetBrains Mono','SF Mono',Menlo,Consolas,monospace",
    "bodySize": "15px",
    "bodyLineHeight": "1.9",
    "bodyWeight": "400",
    "boldWeight": "600",
    "h1Size": "24px",
    "h2Size": "22px",
    "h3Size": "18px",
    "captionSize": "13px",
    "codeSize": "13.5px",
    "chapterLabelSize": "12px",
    "chapterTitleSize": "24px"
  },
  "spacing": {
    "maxWidth": "640px",
    "contentPadding": "16px",
    "paragraphGap": "14px",
    "headingMarginTop": "28px",
    "headingMarginBottom": "16px",
    "chapterPadding": "36px 24px 24px",
    "calloutPadding": "8px 20px",
    "highlightPadding": "16px 20px",
    "borderRadius": "8px",
    "smallRadius": "6px",
    "codeRadius": "3px"
  }
}
```

### Ink Stone Color Rationale
- **Primary #B8553A** — Burnt sienna / terracotta. HSL(14, 52%, 47%). 8 degrees warmer than generic cinnabar, 9 points less saturated. Reads "considered and refined" not "alarming."
- **Text #4A3F3A** — Warm charcoal with red-brown undertone (10.18:1 contrast). Premium print quality.
- **Heading #2C2420** — Near-black with warm undertone (15.21:1 contrast). Never pure #000.
- **Chapter cards** — Sunset Sweep E+ gradient: #4F46E5 靛蓝 → #9333EA 紫 → #DB2777 玫红 → #EA580C 橙 → #CA8A04 琥珀. Follows the natural sunset color spectrum for smooth visual progression. Each chapter transition feels like "the next natural step," not a random jump. Maps to narrative arc: depth → imagination → action → energy → achievement.
- **Code #6B5044** — Warm umber. ONE consistent color for inline and block code.
- **All functional colors** share the warm earth-tone family: warning=#9C6226 (burnt amber), success=#4D7A5C (mineral green), link=#8E5E3E (warm bronze).

---

## Theme: Neon Dusk (霓虹黄昏) — Modern Tech Editorial

Premium tech editorial palette inspired by city skylines at blue hour. Built on a
complementary pair (indigo ~233° vs coral ~15°) with chapter cards forming a sunset
gradient decomposition. Evokes: Stripe docs, Protocol magazine, Linear UI, Apple
"Shot on iPhone" gradients.

```json
{
  "name": "霓虹黄昏 Neon Dusk",
  "colors": {
    "primary": "#3D4ED8",
    "primaryLight": "rgba(61,78,216,0.06)",
    "primaryBorder": "rgba(61,78,216,0.2)",
    "secondary": "#E07A4F",
    "secondaryText": "#B25535",
    "text": "#3B3F54",
    "heading": "#1A1D2E",
    "bold": "#1A1D2E",
    "caption": "#6E7289",
    "link": "#3D4ED8",
    "codeText": "#6E59A5",
    "codeBg": "rgba(110,89,165,0.06)",
    "divider": "rgba(26,29,46,0.15)",
    "cardBorder": "rgba(26,29,46,0.08)",
    "pageBg": "rgba(26,29,46,0.03)",
    "surfaceHighlight": "rgba(61,78,216,0.06)",
    "calloutWarning": "#A86820",
    "calloutWarningBg": "rgba(168,104,32,0.08)",
    "calloutSuccess": "#257A5C",
    "calloutSuccessBg": "rgba(37,122,92,0.08)",
    "chapterPalette": ["#4338A8", "#7C3A96", "#B84460", "#B85234", "#9A6020"],
    "chapterNames": ["Twilight Indigo", "Dusk Violet", "Ember Rose", "Sunset Coral", "Amber Glow"]
  },
  "typography": {
    "body": "'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif",
    "heading": "'Noto Serif SC','Songti SC',STSong,Georgia,serif",
    "code": "'JetBrains Mono','SF Mono',Menlo,Consolas,monospace",
    "bodySize": "15px",
    "bodyLineHeight": "1.9",
    "bodyWeight": "400",
    "boldWeight": "600",
    "h1Size": "24px",
    "h2Size": "22px",
    "h3Size": "18px",
    "captionSize": "13px",
    "codeSize": "13.5px",
    "chapterLabelSize": "12px",
    "chapterTitleSize": "24px"
  },
  "spacing": {
    "maxWidth": "640px",
    "contentPadding": "16px",
    "paragraphGap": "14px",
    "headingMarginTop": "28px",
    "headingMarginBottom": "16px",
    "chapterPadding": "36px 24px 24px",
    "calloutPadding": "8px 20px",
    "highlightPadding": "16px 20px",
    "borderRadius": "8px",
    "smallRadius": "6px",
    "codeRadius": "3px"
  }
}
```

### Neon Dusk Color Rationale
- **Primary #3D4ED8** — Deep electric indigo. Authoritative but modern (6.40:1 contrast).
- **Secondary #E07A4F** — Warm coral for decorative accents only (2.97:1 — NOT for body text). Use #B25535 when coral must be readable text.
- **Chapter cards** — Sunset gradient: deep indigo → violet → rose → coral → amber. Moving from cool to warm mimics a real sunset sweep across the sky.
- **Code #6E59A5** — Muted violet. Feels native to the indigo palette without competing with primary.
- **Text #3B3F54** — Cool blue-gray (subtle blue undertone at ~230°). Harmonizes with indigo primary.

---

## Theme: Cosmic Lavender (寰宇紫) — Deep-Thought Editorial

Premium long-form editorial palette inspired by AI lab / VC research publications
(海外独角兽, Stratechery, Not Boring). Single signature lavender accent on a neutral
warm cream + slate base. Built around **light-weight typography** (PingFang Light) at
**generous line-height 2.0** — the airy, reads-like-a-book feel that signals "this is
a serious cognitive piece." Evokes: Anthropic blog, Notion docs, Substack longform,
academic preprints rebodied for mobile.

```json
{
  "name": "寰宇紫 Cosmic Lavender",
  "colors": {
    "primary": "#7973F7",
    "primaryLight": "rgba(163,140,239,0.20)",
    "primaryBorder": "rgba(121,115,247,0.25)",
    "secondary": "#1B47DC",
    "text": "#2D2C2F",
    "heading": "#000000",
    "bold": "#000000",
    "caption": "#7A7A7A",
    "link": "#1B47DC",
    "codeText": "#444444",
    "codeBg": "#F5F5F5",
    "divider": "#D4D4D4",
    "softDivider": "#EFECE7",
    "cardBorder": "#E8ECF0",
    "pageBg": "#FFFFFF",
    "surfaceHighlight": "rgba(163,140,239,0.20)",
    "calloutWarning": "#A86820",
    "calloutWarningBg": "rgba(168,104,32,0.08)",
    "calloutSuccess": "#257A5C",
    "calloutSuccessBg": "rgba(37,122,92,0.08)",
    "chapterPalette": ["#7973F7", "#1B47DC", "#9D6BE5", "#5664DE", "#3D86E0"],
    "chapterNames": ["Lavender 寰宇紫", "Electric 电光蓝", "Iris 鸢尾", "Periwinkle 长春花", "Azure 远空"]
  },
  "typography": {
    "body": "PingFangSC-light,'PingFang SC','Noto Sans SC','Microsoft YaHei',-apple-system,sans-serif",
    "heading": "PingFangSC-light,'PingFang SC','Noto Sans SC','Microsoft YaHei',-apple-system,sans-serif",
    "english": "Optima-Regular,'Optima','PingFangTC-light','PingFang TC',Georgia,serif",
    "code": "'JetBrains Mono','SF Mono',Menlo,Consolas,monospace",
    "bodySize": "15px",
    "bodyLineHeight": "2",
    "bodyWeight": "300",
    "boldWeight": "600",
    "h1Size": "32px",
    "h2Size": "32px",
    "h3Size": "20px",
    "captionSize": "13px",
    "codeSize": "13.5px",
    "chapterLabelSize": "55px",
    "chapterTitleSize": "32px"
  },
  "spacing": {
    "maxWidth": "640px",
    "contentPadding": "16px",
    "paragraphGap": "0px",
    "paragraphBreakGap": "1em",
    "headingMarginTop": "48px",
    "headingMarginBottom": "24px",
    "chapterPadding": "32px 16px 16px",
    "calloutPadding": "16px 20px",
    "highlightPadding": "16px 20px",
    "borderRadius": "0px",
    "smallRadius": "0px",
    "codeRadius": "3px"
  }
}
```

### Cosmic Lavender Color Rationale
- **Primary #7973F7** — Signature "信仰紫" (belief lavender). HSL(243, 88%, 71%). Bright but not saturated-cheap; reads as "thoughtful technology brand," not "consumer app." This is the article's identity color — used on every accent, every vertical rule, every serial number.
- **First-line highlight rgba(163,140,239,0.20)** — A distinctive trick: the **opening sentence** of each section gets a translucent lavender wash behind the text (not a box, just a marker pen highlight). Signals "thesis sentence — read this carefully."
- **Secondary #1B47DC** — Deep electric blue for secondary callouts and external links. Cooler/more authoritative than the lavender; balances it.
- **Text #2D2C2F** — Near-black cool gray. Pairs with light-weight font for "ink on cream" feel.
- **Soft divider #EFECE7** — Warm cream 1px hairlines. Used as sectioning instead of hard `---` lines; creates pages-of-a-book pacing.
- **Card border #E8ECF0** — Cool pale slate. Used on three sides of the asymmetric quote box (the fourth side is the purple left rail).
- **Code bg #F5F5F5** — Neutral light gray. Code is de-emphasized vs. body, opposite of dev-doc themes.

### Cosmic Lavender Typographic Rules (load-bearing!)
- **Use PingFang LIGHT (300) for body AND headings.** Differentiate hierarchy by SIZE not by WEIGHT. This is the soul of the style — heavier weights immediately make it look like a different (lesser) magazine.
- **Body line-height: 2.0** (not 1.6, not 1.9 — full 2). Extreme breathing room is non-negotiable.
- **Paragraphs separated by blank `<p><br></p>` lines, not margins.** Match the WeChat editor's native rhythm.
- **Section serial number: 55px purple "01." → blank line → 32px Light Bold Title.** This two-line stamp is the visual centerpiece of every section.
- **English/Latin text and author bylines: Optima Regular.** Optima's humanist proportions complement PingFang Light better than Helvetica/Inter would.
- **No serif anywhere.** Unlike Ink Stone, this theme is fully sans — the "weight = light, size = large" hierarchy carries the editorial feel without serifs.

---

## Custom Themes

To create a custom theme, copy any theme JSON above and modify the color values.
Save as a `.json` file and reference via `--theme /path/to/theme.json`.

### Design Guidelines for Custom Themes
1. Keep chapter card colors at medium saturation (S: 35-55% in HSL) — too saturated feels cheap
2. Alternate warm/cool in the chapter palette for visual rhythm
3. Use ONE code color across inline and block
4. All text colors must pass WCAG AA (4.5:1 contrast vs white)
5. Background tints must use rgba() with opacity 0.03-0.08 for dark mode safety
6. Functional colors (warning/success) should share the palette's undertone family

---

## Choosing a Theme

| Theme | Best for | Personality |
|-------|----------|-------------|
| **Ink Stone 墨石** | Translations, philosophical essays, craft/design pieces, Anthropic-style content. | Warm, considered, hand-set print. |
| **Neon Dusk 霓虹黄昏** | Product launches, dev tools, technical announcements, modern SaaS. | Cool, premium, Stripe/Linear. |
| **Cosmic Lavender 寰宇紫** | Deep-thought analysis, company teardowns, science explainers, brand/product PR longform, AI research commentary. | Editorial, airy, "this is a serious cognitive piece." |
