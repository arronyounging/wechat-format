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
