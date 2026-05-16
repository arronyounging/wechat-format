# WeChat Article HTML/CSS Constraints

## Rendering Environment
- Articles render in WebView (WKWebView on iOS, X5/Chromium on Android)
- Content area approximately 375px wide on mobile
- No responsive CSS possible

## MUST DO
- All CSS must be inline `style=""` attributes on every element
- Use `<section>` as the primary structural element (not `<div>`)
- Use `word-break:break-all` on all text elements for CJK wrapping
- Set image dimensions via inline `style` (not HTML `width`/`height` attributes)
- Convert external links to footnote references (only `mp.weixin.qq.com` links are clickable)
- Use `rgba()` for backgrounds (dark mode safe, never hardcode `#fff`)
- Wrap tables with `overflow-x:auto;-webkit-overflow-scrolling:touch`

## MUST NOT USE
- `<style>` tags or external CSS — stripped on save
- `<script>` tags or event handlers — stripped entirely
- `<div>` — use `<section>` instead
- `<ul>`, `<ol>`, `<li>` — WeChat resets list styles; use section + span prefix
- `<table>`, `<tr>`, `<td>`, `<th>` — use `display:table` / `display:table-cell` on sections
- `<blockquote>` — use section with border-left instead
- `position: fixed` or `position: absolute` — stripped/ignored
- CSS variables `var(--xxx)` — not resolved; must use literal values
- `calc()` expressions — must be pre-computed
- `@media` queries — stripped
- `@font-face` — custom fonts not supported; system fonts only
- `@keyframes` / CSS animations — not supported
- `::before` / `::after` pseudo-elements — unreliable
- CSS Grid — unreliable across WeChat versions
- External image URLs in final output — must be on WeChat CDN or auto-fetchable

## SAFE CSS PROPERTIES
- `font-family`, `font-size`, `font-weight`, `font-style`
- `color`, `background-color`, `background` (solid/rgba only)
- `line-height`, `letter-spacing`, `text-align`, `text-indent`, `text-decoration`
- `margin`, `padding` (all sides)
- `border`, `border-left`, `border-top`, `border-bottom`, `border-right`
- `border-radius`
- `display: block`, `display: inline-block`, `display: flex`, `display: table`, `display: table-cell`
- `width`, `max-width`, `height`
- `overflow`, `overflow-x`, `overflow-y`
- `-webkit-overflow-scrolling: touch`
- `opacity`
- `transform`, `transform-origin` (basic usage)
- `vertical-align`
- `white-space`
- `box-shadow` (basic)

## SYSTEM FONTS AVAILABLE
- Chinese: PingFang SC (iOS), Noto Sans CJK (Android), Microsoft YaHei (Windows)
- Serif: Songti SC, STSong, Georgia, Times New Roman
- Monospace: Menlo, Monaco, Consolas, Courier New
- Sans-serif: -apple-system, BlinkMacSystemFont, Helvetica Neue

## IMAGE RULES
- Images must be hosted on `mmbiz.qpic.cn` (WeChat CDN) for published articles
- External URLs may be auto-fetched by WeChat editor on paste, but not guaranteed
- Use `style="max-width:100%;display:block;"` for responsive images
- GIF: max 300 frames, 10MB limit

## CONTENT LIMITS
- Article content: max 20,000 characters, under 1MB total
- Title: max 32 characters
- Digest/summary: max 128 characters
