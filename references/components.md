# WeChat Article Components — 20 HTML Templates

> All color/font/spacing values below use the **Ink Stone** theme as examples.
> Replace with the corresponding design tokens when rendering with a different theme.
> All CSS must be inline. Use `<section>` instead of `<div>`.

---

## 1. Source Block (来源引用块)

**Trigger:** `:::source` fence or article-opening metadata paragraph

```html
<section style="background:rgba(44,36,32,0.03);padding:0;">
  <section style="max-width:640px;margin:0 auto;padding:24px 16px 12px;">
    <p style="font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;font-size:12px;color:#B8553A;letter-spacing:2px;text-transform:uppercase;margin:0 0 8px;word-break:break-all;">FROM ANTHROPIC</p>
  </section>
  <section style="max-width:640px;margin:0 auto;padding:0 16px;">
    <section style="border-top:1px solid rgba(44,36,32,0.15);height:0;"><br></section>
  </section>
  <section style="max-width:640px;margin:0 auto;padding:20px 16px 32px;">
    <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:13px;color:#7A6D66;line-height:1.75;margin:0 0 8px;word-break:break-all;">翻译/来源说明文字</p>
    <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:13px;color:#7A6D66;line-height:1.75;margin:0 0 24px;word-break:break-all;">原文链接：url</p>
    <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:15px;color:#4A3F3A;line-height:1.9;margin:0 0 24px;word-break:break-all;">导语/摘要段落</p>
  </section>
</section>
```

---

## 2. Chapter Card (章节卡片)

**Trigger:** `:::chapter` fence

Color rotates from `chapterPalette` by index.

```html
<section style="max-width:640px;margin:0 auto;padding:0;">
  <section style="background:#4F46E5;border-radius:8px;padding:36px 24px 24px;margin:0 16px;text-align:left;">
    <p style="font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;font-size:12px;color:rgba(255,255,255,0.7);letter-spacing:1px;margin:0 0 4px;word-break:break-all;">Chapter 1</p>
    <p style="font-family:'Noto Serif SC','Songti SC',STSong,Georgia,serif;font-size:24px;font-weight:700;color:rgba(255,255,255,0.95);line-height:1.3;margin:0 0 6px;word-break:break-all;">中文标题</p>
    <p style="font-family:Georgia,'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:13px;color:rgba(255,255,255,0.5);line-height:1.4;margin:0;word-break:break-all;font-style:italic;">English Subtitle</p>
  </section>
</section>
```

---

## 3. Table of Contents (目录)

**Trigger:** `:::toc` fence or `[TOC]` marker

```html
<section style="max-width:640px;margin:0 auto;padding:20px 16px 24px;">
  <h3 style="font-family:'Noto Serif SC','Songti SC',STSong,Georgia,serif;font-size:18px;font-weight:600;line-height:1.4;color:#2C2420;margin:28px 0 6px;word-break:break-all;">目录</h3>
  <section style="background:rgba(255,255,255,0.12);border:1px solid rgba(44,36,32,0.15);border-radius:8px;padding:2px 18px;margin:14px 0;">
    <!-- Each entry: -->
    <section style="padding:14px 0;border-bottom:1px solid rgba(44,36,32,0.15);">
      <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:15px;color:#4A3F3A;margin:0;line-height:1.8;word-break:break-all;">
        <strong style="color:#2C2420;font-weight:600;margin-right:10px;">01</strong>章节名称
      </p>
    </section>
    <!-- Last entry has no border-bottom: -->
    <section style="padding:14px 0;">
      <p style="...">
        <strong style="...">07</strong>最后章节
      </p>
    </section>
  </section>
</section>
```

---

## 4. Section Heading H2

**Trigger:** Markdown `## 标题`

```html
<h2 style="font-family:'Noto Serif SC','Songti SC',STSong,Georgia,serif;font-size:22px;font-weight:700;line-height:1.4;color:#B8553A;margin:18px 0 8px;word-break:break-all;">标题文字</h2>
```

---

## 5. Subsection Heading H3

**Trigger:** Markdown `### 标题`

```html
<h3 style="font-family:'Noto Serif SC','Songti SC',STSong,Georgia,serif;font-size:18px;font-weight:600;line-height:1.4;color:#2C2420;margin:28px 0 16px;word-break:break-all;">
  <span style="color:#B8553A;">标题文字</span>
</h3>
```

---

## 6. Body Paragraph

**Trigger:** Normal Markdown paragraph

```html
<p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:15px;color:#4A3F3A;line-height:1.9;margin:0 0 14px;word-break:break-all;">段落文字</p>
```

---

## 7. Bold Emphasis

**Trigger:** `**加粗**`

```html
<strong style="color:#2C2420;font-weight:600;">加粗文字</strong>
```

---

## 8. Accent Emphasis (主色加粗)

**Trigger:** `***重点***` or `:::accent` inline

```html
<span style="color:#B8553A;font-weight:bold;">强调文字</span>
```

---

## 9. Inline Code

**Trigger:** `` `code` ``

```html
<code style="font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;font-size:13.5px;color:#6B5044;background:rgba(107,80,68,0.06);padding:1px 5px;border-radius:3px;">code</code>
```

---

## 10. Code Block

**Trigger:** ` ```language ... ``` `

```html
<section style="max-width:640px;margin:14px auto;padding:0 16px;">
  <section style="background:rgba(26,26,24,0.04);border-radius:8px;padding:16px 20px;overflow-x:auto;-webkit-overflow-scrolling:touch;">
    <pre style="margin:0;padding:0;font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;font-size:13px;color:#4A3F3A;line-height:1.6;white-space:pre-wrap;word-break:break-all;">
      <code style="font-family:inherit;font-size:inherit;color:inherit;background:transparent;padding:0;">代码内容（保持缩进和换行）</code>
    </pre>
  </section>
</section>
```

Note: WeChat does not support highlight.js class-based highlighting. Code blocks use plain color display. For keyword highlighting, wrap keywords with inline `<span style="color:...">`.

---

## 11. Callout Box (提示框 / 练习框)

**Trigger:** `> ` blockquote or `:::callout` / `:::tip` / `:::exercise`

```html
<section style="background:rgba(255,255,255,0.12);border-left:3px solid #B8553A;padding:8px 20px;margin:0 0 14px;border-radius:0 6px 6px 0;">
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:14px;color:#4A3F3A;line-height:1.8;margin:0;word-break:break-all;">提示/练习内容</p>
</section>
```

**Variant -- Warning (警告):**
border-left color changes to `#e6a23c` (amber)

**Variant -- Success (成功):**
border-left color changes to `#67c23a` (green)

---

## 12. Highlight Box (高亮框)

**Trigger:** `:::highlight` or `:::important`

```html
<section style="background:rgba(184,85,58,0.06);border-radius:8px;padding:16px 20px;margin:14px 0;">
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:15px;color:#B8553A;line-height:1.9;margin:0;text-align:center;word-break:break-all;">核心观点文字</p>
</section>
```

---

## 13. Arrow List (箭头列表)

**Trigger:** `:::steps` fence with list items, or lists starting with `→`

```html
<!-- Each item (not last): -->
<section style="padding:10px 0 10px;border-bottom:1px solid rgba(44,36,32,0.15);">
  <p style="font-size:15px;color:#4A3F3A;margin:0;line-height:1.8;word-break:break-all;">
    <span style="font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;font-size:13px;color:#B8553A;margin-right:8px;">→</span>
    <strong style="color:#2C2420;font-weight:600;margin-right:10px;">标题</strong>描述文字
  </p>
</section>
<!-- First item: padding changes to 0 0 10px; Last item: padding changes to 10px 0 14px with no border-bottom -->
```

---

## 14. Numbered List (编号列表)

**Trigger:** Markdown `1. 2. 3.` ordered list

```html
<section style="padding:10px 0 10px;border-bottom:1px solid rgba(44,36,32,0.15);">
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:15px;color:#4A3F3A;margin:0;line-height:1.8;word-break:break-all;">
    <strong style="color:#2C2420;font-weight:600;margin-right:10px;">01</strong>列表内容
  </p>
</section>
```

---

## 15. Bullet List (无序列表)

**Trigger:** Markdown `- item` unordered list

```html
<section style="padding:8px 0;">
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:15px;color:#4A3F3A;margin:0;line-height:1.8;word-break:break-all;">
    <span style="color:#B8553A;margin-right:8px;">●</span>列表内容
  </p>
</section>
```

---

## 16. CSS Table (表格)

**Trigger:** Markdown table `| a | b |`

```html
<section style="margin:14px 0;overflow-x:auto;-webkit-overflow-scrolling:touch;">
  <!-- Header row -->
  <section style="display:table;width:100%;table-layout:fixed;background:rgba(26,26,24,0.04);border-bottom:1px solid rgba(44,36,32,0.15);">
    <section style="display:table-cell;padding:12px 14px;vertical-align:top;width:33%;">
      <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:13.5px;font-weight:600;color:#2C2420;line-height:1.6;margin:0;word-break:break-all;">表头</p>
    </section>
    <!-- More table-cell... -->
  </section>
  <!-- Data row -->
  <section style="display:table;width:100%;table-layout:fixed;border-bottom:1px solid rgba(44,36,32,0.15);">
    <section style="display:table-cell;padding:12px 14px;vertical-align:top;width:33%;">
      <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:14px;color:#4A3F3A;line-height:1.6;margin:0;word-break:break-all;">数据</p>
    </section>
  </section>
</section>
```

Column width auto-distributes based on column count (2 columns = 50% each, 3 = 33%, 4 = 25%, etc.).

---

## 17. Divider (分割线)

**Trigger:** Markdown `---`

```html
<section style="max-width:640px;margin:0 auto;padding:0 16px;">
  <section style="border-top:1px solid rgba(44,36,32,0.15);height:0;"><br></section>
</section>
```

---

## 18. Image (图片)

**Trigger:** `![alt](src)`

```html
<section style="max-width:640px;margin:14px auto;padding:0 16px;">
  <img src="IMAGE_URL" alt="描述" style="max-width:100%;border-radius:6px;display:block;margin:0 auto;" />
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:12px;color:#7A6D66;text-align:center;margin:8px 0 0;line-height:1.5;word-break:break-all;">图片说明文字</p>
</section>
```

Note: Images must be uploaded to WeChat CDN or use a publicly accessible URL that WeChat can fetch.

---

## 19. Footnote Section (脚注)

**Trigger:** Auto-generated -- all non-mp.weixin.qq.com external links are collected automatically

Inline reference in body text:
```html
<span>链接文字<sup style="color:#B8553A;font-size:11px;">[1]</sup></span>
```

Footnote section at end of article:
```html
<section style="max-width:640px;margin:0 auto;padding:20px 16px;">
  <section style="border-top:1px solid rgba(44,36,32,0.15);height:0;"><br></section>
</section>
<section style="max-width:640px;margin:0 auto;padding:16px 16px;">
  <h3 style="font-family:'Noto Serif SC','Songti SC',STSong,Georgia,serif;font-size:16px;font-weight:600;color:#2C2420;margin:0 0 12px;word-break:break-all;">参考链接</h3>
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:13px;color:#7A6D66;line-height:2;margin:0;word-break:break-all;">
    <span style="color:#B8553A;font-size:11px;margin-right:4px;">[1]</span> 链接标题：<code style="font-family:'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;font-size:12px;color:#6B5044;background:rgba(107,80,68,0.06);padding:1px 4px;border-radius:2px;">https://example.com/url</code>
  </p>
</section>
```

---

## 20. Author Card (作者卡片)

**Trigger:** `:::author` or auto-generated at end of article

```html
<section style="max-width:640px;margin:0 auto;padding:24px 16px;">
  <section style="border-top:1px solid rgba(44,36,32,0.15);height:0;"><br></section>
</section>
<section style="max-width:640px;margin:0 auto;padding:16px 16px 32px;">
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:13px;color:#7A6D66;line-height:1.75;margin:0;word-break:break-all;">作者名 · 公众号名称</p>
  <p style="font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',-apple-system,sans-serif;font-size:13px;color:#7A6D66;line-height:1.75;margin:4px 0 0;word-break:break-all;">简短个人简介或 slogan</p>
</section>
```

---

## 21. Numbered Section Mark (大字号紫色序号 + 标题) — Cosmic Lavender signature

**Trigger:** Markdown `## 标题` when theme is `cosmiclavender`, OR `:::section 01` fence.

The hero component of Cosmic Lavender: a giant 55px purple "01." sits two lines above
a 32px Light bold title. Replaces the standard H2 entirely for the lavender theme.

```html
<section style="text-align:unset;line-height:0;padding-right:16px;padding-left:16px;box-sizing:border-box;max-width:100%;margin-top:48px;">
  <p style="white-space:normal;box-sizing:border-box;margin:0;padding:0;">
    <span style="font-size:55px;color:#7973F7;font-family:Optima-Regular,'Optima','PingFangTC-light',Georgia,serif;box-sizing:border-box;">
      <strong style="box-sizing:border-box;">01.</strong>
    </span>
  </p>
  <p style="white-space:normal;margin:0;padding:0;"><br></p>
</section>
<section style="text-align:left;font-size:32px;font-family:PingFangSC-light,'PingFang SC','Noto Sans SC',-apple-system,sans-serif;padding:0 16px;box-sizing:border-box;margin-bottom:24px;">
  <p style="margin:0;padding:0;box-sizing:border-box;">
    <strong style="box-sizing:border-box;font-weight:600;color:#000;">Focus 的重要性被低估了</strong>
  </p>
</section>
```

**Numbering rule:** Auto-incremented per `## H2` in document order — `01.`, `02.`, ...
Skip if the heading is `## TL;DR`, `## 目录`, `## 参考链接`, or `## 关于作者`.

---

## 22. Vertical Rail Lead Paragraph (紫色竖条引导段) — Cosmic Lavender signature

**Trigger:** First paragraph after the Section Mark, OR `:::lead` fence.

A 6px×75px purple bar to the left of a paragraph — used for the thesis sentence of a
section or for any "you should slow down and read this" callout. Built with flexbox.

```html
<section style="display:flex;flex-flow:row;align-items:stretch;padding:0;margin:14px 0;box-sizing:border-box;max-width:100%;">
  <section style="display:inline-block;vertical-align:middle;flex:0 0 auto;align-self:center;box-sizing:border-box;">
    <section style="display:inline-block;width:6px;height:75px;vertical-align:top;overflow:hidden;background-color:#7973F7;border-width:0;box-sizing:border-box;"><br></section>
  </section>
  <section style="display:inline-block;vertical-align:middle;flex:1 1 0%;align-self:center;padding:0 13px;box-sizing:border-box;">
    <section style="text-align:justify;font-size:15px;font-family:PingFangSC-light,'PingFang SC',-apple-system,sans-serif;line-height:2;padding:0 16px;color:#2D2C2F;box-sizing:border-box;">
      <p style="white-space:normal;margin:0;padding:0;box-sizing:border-box;">
        <span leaf="">过去一年，Anthropic 可能是整个 AI 行业里最值得研究的一家公司。</span>
      </p>
    </section>
  </section>
</section>
```

**Bar height tuning:** Use `height:75px` for 1–2 lines of lead text, `height:auto` won't
work in WeChat (flex stretch fails on dark mode). For longer leads (3+ lines), use the
**Asymmetric Quote Box (#24)** instead.

---

## 23. Thesis-Sentence Highlight (段首句紫色淡底) — Cosmic Lavender signature

**Trigger:** The first sentence of every paragraph that follows a Section Mark, OR any
sentence wrapped in `==text==` (highlight marker) or `:::thesis` inline.

The signature "marker pen" wash — a translucent lavender background painted ONLY behind
the opening thesis sentence. No box, no border — pure inline span.

```html
<p style="white-space:normal;margin:0;padding:0;font-size:15px;font-family:PingFangSC-light,-apple-system,sans-serif;line-height:2;color:#2D2C2F;">
  <span style="background-color:rgba(163,140,239,0.20);box-sizing:border-box;">
    <span leaf="">首先，从战略上来说，OpenAI 一直更像一家什么都想要的公司。</span>
  </span>
</p>
```

**When to apply automatically:** Only on the FIRST `<p>` after a `## H2` Section Mark.
For all subsequent paragraphs in the section, render normally without the highlight.
Over-using this wash kills its impact.

---

## 24. Asymmetric Quote Box (左紫边引用框) — Cosmic Lavender signature

**Trigger:** Markdown `> blockquote` when theme is `cosmiclavender`, OR `:::quote` fence.

A clean 4-sided box where the LEFT border is a thick 6px purple rail and the other three
sides are 1px pale slate. The hallmark of editorial publications.

```html
<section style="border:1px solid #E8ECF0;border-left:6px solid #7973F7;border-radius:8px;padding:14px 16px;margin:20px auto;background:#FFFFFF;max-width:640px;box-sizing:border-box;">
  <p style="white-space:normal;margin:0;padding:0;font-size:15px;font-family:PingFangSC-light,'PingFang SC',-apple-system,sans-serif;line-height:2;color:#2D2C2F;box-sizing:border-box;">
    <span leaf="">引用内容。Anthropic 的判断是：AI 越是发展，越需要有人专注地把对齐这件事做到极致。</span>
  </p>
</section>
```

**2026-05 spacing alignment with #34 aside:** `border-radius:8px`, `padding:14px 16px`, `margin:20px auto`. The purple left rail naturally curves into a small "leaf" at its top-left and bottom-left corners — that's the intended look (modern editorial), not a bug. Keeps this component visually rhythmically consistent with #34 aside / #35 thesis box while preserving its distinct identity (purple rail + slate 3-sides vs full lavender frame).

**Bold-color rule inside this box:** Any `**bold**` inside the quote body renders **BLACK** `#000` (not the body purple). The purple is already provided by the left rail; promoting body bold to purple would collapse hierarchy.

**Variant — minimalist hairline:** Replace `border-left:6px solid #7973F7` with `border:1px solid #E8ECF0 #E8ECF0 #E8ECF0; border-left:1px solid #7973F7` for a more restrained look.

---

## 25. Cream Hairline Divider (米色细线分隔) — Cosmic Lavender signature

**Trigger:** Markdown `---` when theme is `cosmiclavender`, OR `:::softbreak` fence.

A subtle 1px warm-cream horizontal line — much softer than the standard charcoal divider.
Used between paragraphs within a section to create "pages of a book" pacing without the
hard interruption of a normal `---` rule.

```html
<section style="max-width:640px;margin:0 auto;padding:0 16px;">
  <section style="background-color:#EFECE7;height:1px;box-sizing:border-box;max-width:100%;"><br></section>
</section>
```

**Pair-sandwich variant** — bracket a callout block with two cream lines above + below
for a "boxed but borderless" effect:

```html
<section style="max-width:640px;margin:0 auto;padding:0 16px;">
  <section style="background-color:#EFECE7;height:1px;"><br></section>
</section>
<section style="padding:14px 16px;">
  <p style="font-size:15px;font-family:PingFangSC-light,-apple-system,sans-serif;line-height:2;color:#2D2C2F;margin:0;">内容</p>
</section>
<section style="max-width:640px;margin:0 auto;padding:0 16px;">
  <section style="background-color:#EFECE7;height:1px;"><br></section>
</section>
```

---

## 26. Purple Pill + Rule (紫色短条 + 灰色延伸线) — Cosmic Lavender signature

**Trigger:** `:::label` fence with short label text, OR auto-emit before specific
section types (e.g., "TL;DR", "重点", "结语").

A 6px×20px rounded purple pill on the left + a thin 1px gray line extending to the
right edge. Used as a micro-section opener; functions like a wordless section heading.

```html
<section style="display:flex;flex-flow:row;align-items:center;padding:0 16px;margin:24px 0 12px;box-sizing:border-box;">
  <section style="display:inline-block;width:6px;height:20px;background-color:#7973F7;border-radius:30px;vertical-align:middle;flex:0 0 auto;box-sizing:border-box;"><br></section>
  <section style="flex:1 1 0%;margin-left:8px;box-sizing:border-box;">
    <section style="background-color:#444444;height:1px;"><br></section>
  </section>
</section>
```

**With label variant** — insert a small label between the pill and the rule:

```html
<section style="display:flex;flex-flow:row;align-items:center;padding:0 16px;margin:24px 0 12px;">
  <section style="display:inline-block;width:6px;height:20px;background-color:#7973F7;border-radius:30px;flex:0 0 auto;"><br></section>
  <span style="font-family:Optima-Regular,'Optima',Georgia,serif;font-size:14px;color:#7973F7;letter-spacing:1px;margin:0 12px;">TL;DR</span>
  <section style="flex:1 1 0%;background-color:#D4D4D4;height:1px;"><br></section>
</section>
```

**H3 inline variant (2026-05 — replaces the old two-row "pill + rule / title-below" pattern):**

When an `### H3` carries a pill (e.g. L0–L5 layer markers, company subsections in
a comparison section), render the **entire H3 as a single flex row** of pill +
optional label + title text. **No trailing horizontal rule.** The old two-row
pattern (pill + rule on row 1, title below on row 2) looked like a broken
divider whenever the label-between-pill-and-rule was empty.

```html
<!-- H3 with Optima label (e.g. L0 协议与授权层) -->
<section style="display:flex;flex-flow:row;align-items:center;padding:0 8px;margin:32px auto 16px;box-sizing:border-box;max-width:640px;">
  <section style="display:inline-block;width:6px;height:20px;background-color:#7973F7;border-radius:30px;flex:0 0 auto;"><br></section>
  <span style="font-family:Optima-Regular,'Optima',Georgia,serif;font-size:14px;color:#7973F7;letter-spacing:1px;font-weight:600;margin:0 10px 0 12px;flex:0 0 auto;">L0</span>
  <span style="font-size:17px;font-family:PingFangSC-light,'PingFang SC','Noto Sans SC',-apple-system,sans-serif;font-weight:600;color:#000;line-height:1.5;flex:1 1 0%;">协议与授权层</span>
</section>

<!-- H3 without label (e.g. 阿里 · 从流量平台，到意图经营系统) -->
<section style="display:flex;flex-flow:row;align-items:center;padding:0 8px;margin:32px auto 16px;box-sizing:border-box;max-width:640px;">
  <section style="display:inline-block;width:6px;height:20px;background-color:#7973F7;border-radius:30px;flex:0 0 auto;"><br></section>
  <span style="display:inline-block;width:12px;flex:0 0 auto;"></span>
  <span style="font-size:17px;font-family:PingFangSC-light,'PingFang SC','Noto Sans SC',-apple-system,sans-serif;font-weight:600;color:#000;line-height:1.5;flex:1 1 0%;">阿里 · 从流量平台，到意图经营系统</span>
</section>
```

When to use which:
- **With label** — when the H3 represents a structured marker (L0–L5 architecture layers, Step 01–06 process stages). Optima 14px purple label fills the "gap" semantically.
- **Without label** (12px spacer instead) — when the H3 is a name or phrase (company name, product name, person, concept). The 12px transparent spacer keeps the title text from touching the pill without inventing a meaningless label.

---

## 27. Cosmic Lavender Bullet List (紫色圆点列表)

**Trigger:** Markdown `- item` when theme is `cosmiclavender`.

Replaces the default `●` prefix with a true 10×10 lavender disc rendered as an inline
section block (cleaner kerning than a glyph).

```html
<section style="padding:8px 16px;display:flex;flex-flow:row;align-items:flex-start;box-sizing:border-box;">
  <section style="display:inline-block;width:10px;height:10px;background-color:#7973F7;border-radius:10px;flex:0 0 auto;margin-top:12px;margin-right:10px;box-sizing:border-box;"><br></section>
  <section style="flex:1 1 0%;">
    <p style="font-size:15px;font-family:PingFangSC-light,'PingFang SC',-apple-system,sans-serif;line-height:2;color:#2D2C2F;margin:0;">列表项内容</p>
  </section>
</section>
```

---

## 28. Author Byline (Optima 体作者署名) — Cosmic Lavender signature

**Trigger:** Article-opening byline (replaces the standard Author Card when theme is
`cosmiclavender`), OR `:::byline` fence at top.

A spacious Optima-set byline at the top of the article — distinguishes professional
publications from consumer blog posts.

```html
<section style="text-align:justify;font-size:15px;font-family:Optima-Regular,'Optima','PingFangTC-light','PingFang TC',Georgia,serif;line-height:2;padding:0 16px;margin:24px 0 8px;color:#2D2C2F;box-sizing:border-box;">
  <p style="white-space:normal;margin:0;padding:0;"><span leaf="">作者：Celia</span></p>
  <p style="white-space:normal;margin:0;padding:0;"><span leaf="">编辑：penny</span></p>
  <p style="white-space:normal;margin:0;padding:0;"><span leaf="">排版：Mengxi</span></p>
</section>
```

---

## 34. Cosmic Lavender Knowledge Aside (紫框淡紫底知识盒) — Cosmic Lavender signature

**Trigger:** `:::aside` fence when theme is `cosmiclavender`, with the FIRST line
treated as the lavender-bold title and the remaining lines as the body.

The Cosmic Lavender adaptation of Pine Ink's #31 Knowledge Aside. Same job — an
inline "rest stop" that pulls the reader out of dense argument paragraphs to
introduce a concept, pose a thought experiment, or pull out a definition — but
recolored to the lavender/violet system and tuned for tighter internal padding
since the body text already sits at 8px outer padding.

```html
<section style="font-size:15px;white-space:normal;margin:20px auto;color:#2D2C2F;font-family:PingFangSC-light,'PingFang SC','Noto Sans SC',-apple-system,sans-serif;line-height:2;background-color:#FAF8FF;border:1px solid #7973F7;border-radius:8px;padding:14px 16px;max-width:640px;box-sizing:border-box;">
  <strong style="word-break:break-all;font-weight:600;color:#7973F7;font-size:16px;">
    <span>你知道吗——为什么"寰宇紫"适合做认知型长文主题？</span>
  </strong>
  <span><br/><br/></span>
  <span>寰宇紫的灵感来自 Anthropic、Stratechery、海外独角兽这类深度阅读型出版物。主色 #7973F7 是 HSL(243, 88%, 71%) 的"信仰紫"——明度足以让人"读得下去"，饱和度又能托起"思考型品牌"的语义。</span>
</section>
```

**Color rationale (vs. Pine Ink #31):**
- Border `#7973F7` (signature lavender) replaces sage `#407600`
- Background `#FAF8FF` (very pale violet, ~98% lightness) replaces mint `#F9FDF5`
- Title color `#7973F7` (full primary) replaces sage bold
- All other proportions (8px radius, 15px body, 16px title, `<br/><br/>` paragraph break) carry over unchanged

**Padding rationale (vs. Pine Ink #31):**
Pine Ink uses `16px 20px` because its body text sits at `0 16px` outer padding, so
the 4px inset feels deliberate. Cosmic Lavender body text now sits at `0 8px`
outer padding (tightened for long-form), so the aside box uses a tighter
`14px 16px` internal padding to match — keeps the box from feeling visually
heavier than the surrounding paragraphs.

**Title detection:** First non-empty line becomes the lavender bold title.
Ending the first line with `?` or `？` reads as a "Q-aside" (thought experiment);
ending with anything else reads as a "definition aside." Both render identically.

**Pacing rule:** Same as Pine Ink — one aside every 800–1500 characters of body
text. Three in a row kills the breath; one per ~3 phone-screens of scroll is
the sweet spot.

**Body layout (2026-05 update — no line-count limit, full line/paragraph control):**

- **Each markdown line in the body = one rendered line** (separated from the next by `<br/>`).
- **A blank line in the body = a paragraph break** (rendered as `<br/><br/>`, adds breathing room between paragraphs).
- **No artificial maximum.** The aside can be 1 line, 5 lines, or 20 lines — author decides what fits the content.
- **Inline markdown still works** in body lines — `**bold**` becomes black bold (#000) so it doesn't compete with the purple title.

Example: a 3-paragraph aside with inline-bold acronym names:

```markdown
:::aside
你知道吗——UCP、AP2、Universal Cart 到底是什么？
这是 Google 在 I/O 2026 抛出的 agentic commerce 协议三件套。

**UCP**（Universal Commerce Protocol）让商家把商品、库存、价格、政策以 Agent 可读的格式暴露出来。

**AP2**（Agent Payments Protocol）解决"机器代表人付款"的可验证、可限制、可追责问题。

**Universal Cart** 则提供跨平台的统一购物车，让一次 Agent 操作能跨商家结算。

三件事合在一起，相当于在为 Agent 商业准备 HTTP + OAuth + 支付网关那一层底层基础设施。
:::
```

Renders as: title (purple bold) → blank → intro line → blank → bold-prefixed paragraph → blank → bold-prefixed paragraph → blank → bold-prefixed paragraph → blank → wrap-up line.

The previous "Aim for 2-4 lines" guideline was removed — long asides are now first-class. Use whatever length the content needs.

**Pacing rule (still applies):** Frequency, not length, is what makes asides feel orchestrated. Still aim for one aside every 800–1500 chars of body text; back-to-back asides break the breath.

**Minimal fence syntax:**

```markdown
:::aside
你知道吗——Naval 的三种杠杆？
劳动力、资本、零边际成本复制（代码/媒体）。前两者是上一个时代的杠杆，第三者才是真正的超级个体杠杆。
:::
```

---

## 35. Cosmic Lavender Core Thesis Box (核心论断框) — Cosmic Lavender signature

**Trigger:** Auto-emitted when a whole markdown paragraph is wrapped in `**...**`
(entirely bold). Visually identical to the #34 Knowledge Aside container (rounded
lavender frame), but no title row — the bold body itself IS the punchline.

Replaces the old flat `rgba(163,140,239,0.18)` highlight box, which looked
"out of family" once the rest of the theme moved to rounded lavender containers.

```html
<section style="font-size:15px;white-space:normal;margin:20px auto;color:#2D2C2F;font-family:PingFangSC-light,'PingFang SC','Noto Sans SC',-apple-system,sans-serif;line-height:2;background-color:#FAF8FF;border:1px solid #7973F7;border-radius:8px;padding:14px 16px;max-width:640px;box-sizing:border-box;text-align:justify;">
  <strong style="font-weight:600;color:#000;">更准确地说，是每单位满足感所需要付出的决策成本越低，商业效率越高。</strong>
</section>
```

**Why bold body stays BLACK (not purple):**
The box already declares its emphasis via the lavender frame + lavender background.
If the body bold also went purple `#7973F7`, the entire box would collapse into
monochrome — eye loses the layered semantics ("box = stop here", "bold = read the
exact words"). Black body bold preserves the two-step read: 1) eye is caught by
the lavender frame, 2) eye then reads a high-contrast black sentence.

**Trigger detection:**
- Whole paragraph wrapped in `**...**` (no other text outside the asterisks)
- E.g. `**这是核心论断。**` → renders as #35
- E.g. `这是 **部分加粗** 的段落。` → renders as normal paragraph with purple inline bold (NOT #35)

**Spacing:** Same as #34 aside (`margin:20px auto`, `padding:14px 16px`, `border-radius:8px`) — the two components feel like family.

---

## 36. Cosmic Lavender Reading Card (延伸阅读卡片) — Cosmic Lavender signature

**Trigger:** `:::reading [optional title] ... :::` fence.

A stacked-card "Further Reading" component modeled after WeChat's native 图文卡片
(image-link card). Each card = full-width banner image on top, single-line title
row below with a circular lavender chevron on the right.

**Fence syntax:**

```markdown
:::reading 延伸阅读
https://cdn.example.com/cover1.jpg
Supabase：百亿美元估值，vibe coding 的默认后端？
https://mp.weixin.qq.com/s/xxx

https://cdn.example.com/cover2.jpg
深度讨论新一轮模型发布：当智能进入月更时代 | Best Ideas
https://mp.weixin.qq.com/s/yyy
:::
```

- Each card = exactly 3 consecutive non-blank lines: `image_url` / `title` / `article_url`
- Blank line separates cards
- Optional header text after `:::reading ` renders as #26 Purple Pill + Rule with Optima label
- `image_url = _` or `-` or `placeholder` → renders a lavender-gradient placeholder block (`COVER · 封面图` Optima text) for previewing without real images
- If `article_url` contains `mp.weixin.qq.com`, the entire card becomes a clickable `<a>`; otherwise the card is non-interactive (per the global rule that only `mp.weixin.qq.com` links survive as `<a>`)

**Card HTML template (single card):**

```html
<a href="https://mp.weixin.qq.com/s/xxx" style="text-decoration:none;color:inherit;display:block;">
  <section style="border:1px solid #E8ECF0;border-radius:10px;overflow:hidden;margin:0 auto 16px;background:#FFFFFF;max-width:640px;box-sizing:border-box;font-size:0;line-height:0;">
    <section style="margin:0;padding:0;font-size:0;line-height:0;">
      <img src="https://cdn.example.com/cover.jpg" alt="" style="display:block;width:100%;margin:0;padding:0;border:0;vertical-align:bottom;" />
    </section>
    <section style="display:flex;align-items:center;justify-content:space-between;padding:14px 16px;margin:0;font-size:15px;line-height:1.5;">
      <span style="font-family:PingFangSC-light,'PingFang SC',-apple-system,sans-serif;color:#2D2C2F;flex:1 1 0%;font-size:15px;line-height:1.5;">Supabase：百亿美元估值，vibe coding 的默认后端？</span>
      <span style="display:inline-block;width:24px;height:24px;border-radius:12px;background-color:rgba(121,115,247,0.10);text-align:center;line-height:24px;color:#7973F7;font-size:14px;margin-left:12px;flex:0 0 auto;font-family:Georgia,serif;font-weight:600;">›</span>
    </section>
  </section>
</a>
```

**WeChat editor compatibility — load-bearing rules:**

WeChat's WYSIWYG editor inserts a `<p>` wrapper around lone `<img>` tags by
default, and that `<p>` carries the editor's default paragraph margin (~32px top
+ bottom). On the original draft of this card this produced a ~90px gap between
the image and the title row. The fix is three layers of margin suppression:

1. **Outer card** declares `font-size:0; line-height:0` so any whitespace text
   node WeChat inserts between children collapses to zero height. The title row
   re-declares `font-size:15px; line-height:1.5` to restore visible text.
2. **Image is wrapped in a `<section>`** with `font-size:0; line-height:0; margin:0; padding:0` — this stops WeChat from `<p>`-wrapping the lone `<img>`.
3. **`<img>` itself** uses `display:block; vertical-align:bottom; margin:0; padding:0; border:0` — `vertical-align:bottom` kills the residual inline-baseline 4px gap that `display:block` alone doesn't fix in some renderers.

**Optional header (Purple Pill + Rule above the stack):**

```html
<section style="display:flex;flex-flow:row;align-items:center;padding:0 8px;margin:48px auto 20px;box-sizing:border-box;max-width:640px;">
  <section style="display:inline-block;width:6px;height:22px;background-color:#7973F7;border-radius:30px;flex:0 0 auto;"><br></section>
  <span style="font-family:Optima-Regular,'Optima','PingFangTC-light','PingFang TC',Georgia,serif;font-size:15px;color:#7973F7;letter-spacing:2px;font-weight:600;margin:0 14px;">延伸阅读</span>
  <section style="flex:1 1 0%;background-color:#D4D4D4;height:1px;"><br></section>
</section>
```

**Placement convention:** Reading Cards typically appear at the end of an
article (between the conclusion and the author byline). They can also appear
mid-article when a section references multiple companion pieces — but only
once per article is the usual rhythm.

**Image-URL workflow:**

| Source | URL pattern | Notes |
|--------|-------------|-------|
| WeChat 素材库 (most stable) | `https://mmbiz.qpic.cn/mmbiz_jpg/xxx/640?...` | Manual upload via 公众号 editor → copy URL |
| Your own CDN (most convenient) | `https://cdn.your-domain/covers/xxx.jpg` | When pasted into WeChat editor, the editor usually auto-mirrors external images to its own CDN |
| Any public image host | `https://...` | Same auto-mirror behavior; subject to hot-link protection failures |

**Anti-patterns:**
- Do not put more than 5 cards in one `:::reading` block — readers stop scanning
- Do not use without article URLs — the chevron implies clickability
- Do not use external (non-mp.weixin.qq.com) URLs as the article_url; readers tapping the card would land outside the WeChat ecosystem, which is a poor UX

---

## 29. Pine Chapter Heading (绿色下划线章节标题) — Pine Ink signature

**Trigger:** Markdown `## 标题` when theme is `pineink`, OR `:::pine-chapter` fence.

The hero component of Pine Ink: a centered 24px sage-green bold title sitting on
an 8px solid green underline, with a luxurious 80px of breathing room above. Every
chapter feels like turning a page in a printed essay. Replaces the standard H2
entirely when the theme is active.

```html
<section style="display:block;line-height:1.5;font-size:24px;font-family:'Optima-Regular','Optima','PingFangSC-light','PingFangTC-light','PingFang SC',Cambria,Cochin,Georgia,Times,'Times New Roman',serif;font-weight:bold;margin:80px auto 40px auto;width:fit-content;color:#407600;text-align:center;padding:0 1em;border-bottom:8px solid #407600;letter-spacing:0.1em;word-break:break-all;">
  <span>前言</span>
</section>
```

**Why a `<section>` not an `<h2>`:** WeChat's editor force-restyles `<h2>` tags
(injects its own margin, removes letter-spacing). The reference implementation
deliberately uses `<section>` to bypass this. Pine Ink follows the same approach
— this is structural, not stylistic.

**Spacing rules:**
- First chapter in the article: reduce top margin to `40px` (no need to push down from above)
- Subsequent chapters: full `80px` top margin
- After a Pine Manifesto Opener (#30): full `80px` top margin still applies

---

## 30. Pine Manifesto Opener (灰底绿条立论块) — Pine Ink signature

**Trigger:** First `> blockquote` at the very start of the article when theme is
`pineink`, OR `:::manifesto` fence, OR any explicit `:::callout` placed before the
first `## H2`.

A gray-background block with a 3px green left rail, holding the article's central
claim or thesis sentence in bold sage green. Article-opening "show me the knife"
component — the reader instantly knows what the next 10,000 words will defend.

```html
<section style="line-height:26px;word-spacing:normal;hyphens:auto;text-align:left;outline:0;max-width:100%;border-top:none;border-right:none;border-bottom:none;display:block;overflow:auto;padding:10px 16px;margin:20px 0;border-left:3px solid #407600;background-color:#F5F5F5;font-family:'Optima-Regular','Optima','PingFangSC-light','PingFangTC-light','PingFang SC',Cambria,Cochin,Georgia,Times,'Times New Roman',serif;letter-spacing:0.1em;">
  <p style="text-align:left;line-height:26px;margin:0;letter-spacing:0.1em;color:#407600;font-size:15px;">
    <strong style="font-weight:600;color:#407600;word-break:break-all;">
      <span>超级个体是一种底层人格结构。</span>
    </strong>
  </p>
</section>
```

**Pacing rule:** Use AT MOST ONCE per article. The whole point is that it announces
the thesis — a second one dilutes the first. For multiple key claims mid-article,
use Knowledge Aside (#31) instead.

---

## 31. Knowledge Aside / "你知道吗" Box (绿框薄绿底知识盒) — Pine Ink signature

**Trigger:** `:::aside` fence, with the FIRST line treated as the title (auto
green-bold) and the remaining lines as the body.

The killer feature of Pine Ink. A rounded box with `1px #407600` border, `#F9FDF5`
mint-mist background, and 8px radius. Used as inline "rest stops" every few hundred
words to introduce a concept, pose a thought experiment, or pull out a definition.
Lets a reader's brain breathe between dense argument paragraphs — the single biggest
reason 10k+ character essays in this style don't exhaust the reader.

```html
<section style="font-size:15px;white-space:normal;margin:20px 0;color:#3F3F3F;font-family:'Optima-Regular','Optima','PingFangSC-light','PingFangTC-light','PingFang SC',Cambria,Cochin,Georgia,Times,'Times New Roman',serif;line-height:26px;letter-spacing:0.1em;background-color:#F9FDF5;border:1px solid #407600;border-radius:8px;padding:16px 20px;">
  <strong style="word-break:break-all;font-weight:600;color:#407600;">
    <span>你知道吗——Naval 的三种杠杆？</span>
  </strong>
  <span><br/><br/></span>
  <span>劳动力、资本、零边际成本复制（代码/媒体）。前两者是上一个时代的杠杆，第三者才是真正的超级个体杠杆。Naval 在 2018 年那条推就把这件事说完了——只是大多数人当时没听懂。</span>
</section>
```

**Fence syntax:**

```markdown
:::aside
你知道吗——Naval 的三种杠杆？
劳动力、资本、零边际成本复制（代码/媒体）。前两者是上一个时代的杠杆，第三者才是真正的超级个体杠杆。
:::
```

**Title detection:** The first non-empty line becomes the green bold title. If the
first line ends with `?` or `？` (Chinese), the box is rendered as a "Q-aside"
(thought-experiment framing). Otherwise it's rendered as a "definition aside."
Both render identically — the distinction is purely semantic for the author.

**Pacing rule:** Aim for one aside every 800–1500 characters of body text in a
long essay. Spacing them is what creates rhythm. Three asides back-to-back kills
the breath; one aside per 3 pages of reading is the sweet spot.

**Multi-paragraph body:** Separate paragraphs inside an aside with `<br/><br/>`
inline (NOT separate `<p>` blocks — keeps the box visually unified):

```html
<span>第一段内容。</span>
<span><br/><br/></span>
<span>第二段内容。</span>
```

---

## 32. Pine Author Byline (右对齐作者署名) — Pine Ink signature

**Trigger:** `:::byline` fence when theme is `pineink`, OR auto-emitted at the top
of the article when `author` is in frontmatter.

A right-aligned single-line byline with an emoji prefix. Sits below the manifesto
opener (#30) or directly under the title image, before the first chapter heading.
Distinguishes the literary-essay register from a corporate blog post.

```html
<p style="text-align:right;line-height:26px;font-family:'Optima-Regular','Optima','PingFangSC-light','PingFangTC-light','PingFang SC',Cambria,Cochin,Georgia,Times,'Times New Roman',serif;margin:0;padding-bottom:1em;letter-spacing:0.1em;white-space:pre-line;color:#3F3F3F;font-size:15px;">
  <span>👦🏻 作者:&nbsp;</span><span>Henry</span>
</p>
```

**Multi-credit variant** — for articles with multiple contributors, stack roles
on separate lines (each on its own `<p>` with the same style):

```html
<p style="...">👦🏻 作者:&nbsp;Henry</p>
<p style="...">✏️ 编辑:&nbsp;Penny</p>
<p style="...">🎨 排版:&nbsp;Mengxi</p>
```

**Emoji convention:** Use a single emoji per role as a visual icon. 👦🏻/👧🏻 for
author, ✏️ for editor, 🎨 for art/layout, 📷 for photography, 🎙️ for interview,
🗣️ for translator. Skin tone is optional but recommended for warmth.

---

## 33. Pine Footnote (松烟版脚注) — Pine Ink override

**Trigger:** Auto-generated, same as #19 but with Pine Ink color hierarchy.

Three-tier muted gray classic editorial footnote — index `#222` bold, label `#555`,
URL `#888`. 12px size, 1.7 line-height (slightly tighter than body for "small print"
register). Replaces #19 when theme is `pineink`.

```html
<section style="max-width:640px;margin:0 auto;padding:20px 16px 8px;">
  <section style="background-color:#E5E5E5;height:1px;letter-spacing:0.1em;"><br/></section>
</section>
<section style="max-width:640px;margin:0 auto;padding:8px 16px 16px;">
  <p style="font-family:'Optima-Regular','Optima','PingFangSC-light','PingFangTC-light','PingFang SC',Cambria,Cochin,Georgia,Times,'Times New Roman',serif;font-size:14px;color:#222222;font-weight:600;letter-spacing:0.1em;margin:0 0 12px;word-break:break-all;">参考链接</p>
  <p style="font-size:12px;color:#555555;line-height:1.7;margin:.3em 0;word-break:break-all;letter-spacing:0.1em;font-family:'Optima-Regular','Optima','PingFangSC-light','PingFangTC-light','PingFang SC',Cambria,Cochin,Georgia,Times,'Times New Roman',serif;">
    <span style="color:#222222;font-weight:bold;margin-right:4px;"><span>[1]</span></span>
    <span>链接说明文字：</span>
    <span style="color:#888888;"><span>https://example.com/url</span></span>
  </p>
</section>
```

**Inline reference style** (in body text):

```html
<span>引用文字</span><sup style="font-size:.7em;color:#222222;font-weight:bold;line-height:0;vertical-align:super;letter-spacing:0;"><span>[1]</span></sup>
```

Note: superscript `[N]` is in `#222` bold (not the sage primary) — keeps the
footnote markers from competing with the green accent. The sage is reserved for
headings, manifesto, and asides — three load-bearing places, no more.

---

## Pine Ink — Assembly Cheat Sheet

When theme = `pineink`, override the standard mappings as follows:

| Markdown | Standard component | Pine Ink component |
|----------|---------------------|---------------------|
| `## Heading` | #4 Section Heading H2 | **#29 Pine Chapter Heading** (sage + 8px underline + 80px top margin) |
| `### Heading` | #5 Subsection H3 | H3 stays — 17px, sage `#407600`, **font-weight: 600**, margin `40px 0 16px`, NOT centered, NO underline (subtler than #29) |
| First `>` blockquote in article | #11 Callout Box | **#30 Pine Manifesto Opener** (only once per article) |
| Subsequent `>` blockquote | #11 Callout Box | #11 with sage colors (border-left `3px solid #407600`, bg `#F5F5F5`) |
| `:::aside` | (n/a in other themes) | **#31 Knowledge Aside** |
| `:::manifesto` | (n/a) | **#30 Pine Manifesto Opener** (explicit trigger) |
| `:::byline` | #20 Author Card | **#32 Pine Author Byline** (right-aligned, top of article) |
| `- bullet` | #15 Bullet List | #15 with sage `#407600` disc prefix |
| `1. number` | #14 Numbered List | #14 with sage `#407600` digit prefix |
| Footnotes | #19 | **#33 Pine Footnote** |
| `**bold**` | #7 (heading color) | #7 with color `#222222` (NOT sage — sage reserved for accents only) |
| `***accent***` | #8 (primary color) | #8 with color `#407600` (sage) |
| `---` divider | #17 Divider | #17 with color `#E5E5E5` (softer than default charcoal) |
| `:::chapter` | #2 Chapter Card | **Disabled** — Pine Ink doesn't use colored chapter cards. Auto-convert to #29 Pine Chapter Heading using the chapter's main title text. |

All paragraphs (universal across Pine Ink):
- font-family: `'Optima-Regular','Optima','PingFangSC-light','PingFangTC-light','PingFang SC',Cambria,Cochin,Georgia,Times,'Times New Roman',serif` (single shared stack)
- font-size: `15px`
- color: `#3F3F3F`
- line-height: `1.75` (or `26px` literal — prefer literal in inline styles)
- **letter-spacing: `0.1em`** (REQUIRED on every text element — body, headings, captions, code, footnotes, links, asides; the only exception is `<sup>` footnote markers which use `letter-spacing:0` to keep the bracket+digit tight)
- margin: `20px 0` (real margin, NOT blank `<p><br></p>` separators)
- text-align: `left` (NOT justify — left-align reads more like a manuscript)
- padding: `0 16px` (when paragraph is wrapped in the content `<section>`; bare `<p>` inside boxes have padding from the box)
- word-wrap: `break-word`

All H3 subheadings (Pine Ink):
- font-family: same shared stack
- font-size: `17px`
- font-weight: `600`
- color: `#407600`
- letter-spacing: `0.1em`
- margin: `40px 0 16px`
- NO underline, NO centering — keeps the sage `border-bottom` reserved exclusively for #29 chapter marks

Image (Pine Ink override):
- `border-radius: 10px` (NOT the default 6px — slightly larger, matches the reference article)
- No caption by default (reference article omits captions; if `alt` text is meaningful, render a 12px `#888` caption underneath in the same Optima/PingFang stack with `letter-spacing:0.1em`)
- Wrapper: `<section style="margin:15px 0;text-align:center;">`

Disabled in Pine Ink (do NOT auto-emit):
- TOC (`:::toc`) — Pine Ink essays read linearly; a TOC fragments the meditative pace
- Numbered serial marks (Cosmic Lavender's `01.`, `02.`)
- First-sentence marker-pen highlight (Cosmic Lavender's #23)
- Chapter color rotation (single sage accent only)

---

## Cosmic Lavender — Assembly Cheat Sheet

When theme = `cosmiclavender`, override the standard mappings as follows:

| Markdown | Standard component | Cosmic Lavender component |
|----------|---------------------|----------------------------|
| `## Heading` | #4 Section Heading H2 | **#21 Numbered Section Mark** (with auto 01., 02., ...) |
| First `<p>` after `## H2` | #6 Body Paragraph | **#23 Thesis-Sentence Highlight** (wrap first sentence) |
| `> quote` | #11 Callout Box | **#24 Asymmetric Quote Box** |
| `---` | #17 Divider | **#25 Cream Hairline Divider** |
| `- item` | #15 Bullet List | **#27 Lavender Disc Bullet** |
| `:::lead` | (n/a) | **#22 Vertical Rail Lead Paragraph** |
| `:::label TEXT` | (n/a) | **#26 Purple Pill + Rule** |
| `:::byline` | #20 Author Card | **#28 Optima Author Byline** (top of article) |
| `:::aside` | (n/a in other themes) | **#34 Cosmic Lavender Knowledge Aside** (multi-paragraph supported) |
| `**inline bold**` | #7 black bold | **purple bold `#7973F7`** (theme accent — body only; black inside any lavender container) |
| `**整段全粗**` | flat tinted highlight box | **#35 Core Thesis Box** (rounded lavender container, bold body stays black) |
| `:::reading` | (n/a in other themes) | **#36 Cosmic Lavender Reading Card** (image + title + chevron stack) |
| `### H3` (with `:::label X` pill prefix) | #5 H3 + #26 pill above | **single-row inline pattern**: `[pill][label][title]`, NO trailing rule |
| H2 + preceding `---` | divider + H2 | render the `---` divider only; H2 adds no extra divider (avoids double-line stacking) |

All paragraphs:
- font-family: `PingFangSC-light,'PingFang SC',-apple-system,sans-serif`
- font-size: `15px`
- line-height: `2`
- color: `#2D2C2F`
- text-align: `justify`
- padding: `0 8px` (tightened from 16px in 2026-05 for long-form readability)
- Separated by `<p style="margin:0;"><br></p>` blank lines, NOT margin-bottom.

All headings (including #21):
- font-family: `PingFangSC-light` (Light weight, NOT bold or regular)
- Differentiate hierarchy by SIZE not WEIGHT — 32px (or 30px) Light bold for H2, **17px** Light bold for H3 (tightened from 20-22px in 2026-05; the wider H2/H3 gap restores clearer subordination).

Bold color hierarchy (2026-05 rule — added to keep theme cohesion as the article scales):
1. **Inline `**bold**` in body paragraph** → `#7973F7` purple bold. Acts like a low-cost highlighter — the reader's eye latches onto the violet word.
2. **`**整段全粗**` (whole paragraph)** → renders as #35 Core Thesis Box; bold body inside stays `#000` black (the purple is already provided by the box border and background, so the bold doesn't need to color-shift).
3. **Bold inside a #34 Knowledge Aside body** → stays `#000` black. The aside title is already purple bold; making body bold also purple makes the whole box monochromatic and the title stops feeling like a label.
4. **Bold inside the asymmetric quote box (#24)** → keep `#000` black for the same reason.

This 4-rule hierarchy is what makes purple feel "spent meaningfully" instead of "splashed everywhere." Roughly: purple bold for **emphasis in the white-space of body text**; black bold for **emphasis inside an already-purple container**.

---

## Content Wrapper Structure

The entire article is wrapped in a unified outer structure:

```html
<section style="background:rgba(44,36,32,0.03);padding:0;">
  <!-- Source Block (if applicable) -->
  <!-- Chapter Card (if applicable) -->
  <!-- Content sections, each wrapped in: -->
  <section style="max-width:640px;margin:0 auto;padding:16px 16px;">
    <!-- paragraphs, headings, components -->
  </section>
  <!-- Divider between major sections -->
  <!-- More content sections... -->
  <!-- Footnotes (if applicable) -->
  <!-- Author Card (if applicable) -->
</section>
```
