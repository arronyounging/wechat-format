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
<section style="border:1px solid #E8ECF0;border-left:6px solid #7973F7;padding:16px 20px;margin:14px 0;background:#FFFFFF;box-sizing:border-box;">
  <p style="white-space:normal;margin:0;padding:0;font-size:15px;font-family:PingFangSC-light,'PingFang SC',-apple-system,sans-serif;line-height:2;color:#2D2C2F;box-sizing:border-box;">
    <span leaf="">引用内容。Anthropic 的判断是：AI 越是发展，越需要有人专注地把对齐这件事做到极致。</span>
  </p>
</section>
```

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

All paragraphs:
- font-family: `PingFangSC-light,'PingFang SC',-apple-system,sans-serif`
- font-size: `15px`
- line-height: `2`
- color: `#2D2C2F`
- text-align: `justify`
- padding: `0 16px`
- Separated by `<p style="margin:0;"><br></p>` blank lines, NOT margin-bottom.

All headings (including #21):
- font-family: `PingFangSC-light` (Light weight, NOT bold or regular)
- Differentiate hierarchy by SIZE not WEIGHT — 32px Light bold for H2, 20px Light bold for H3.

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
