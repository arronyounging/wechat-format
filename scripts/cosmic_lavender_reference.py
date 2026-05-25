#!/usr/bin/env python3
"""Convert a Markdown article to Cosmic Lavender WeChat HTML."""
import re
import sys
import os
from pathlib import Path

MD_PATH = "/Users/arronyoung/Downloads/离开京东后_我重新理解了AI时代电商的第一性原理_最终版.md"
OUT_PATH = "/Users/arronyoung/Downloads/离开京东后_我重新理解了AI时代电商的第一性原理_最终版-wechat.html"
PREVIEW_PATH = "/tmp/wechat-article-preview.html"
TEMPLATE = "/Users/arronyoung/.claude/skills/wechat-format/scripts/copy-to-clipboard.html"

# Sections to NOT auto-number
NO_NUMBER_HEADINGS = {"TL;DR", "目录", "参考链接", "关于作者", "写在最后",
                     "先说结论", "结语"}

PURPLE = "#7973F7"
THESIS_BG = "rgba(163,140,239,0.30)"
HIGHLIGHT_BG = "rgba(163,140,239,0.18)"
CREAM = "#EFECE7"
TEXT = "#2D2C2F"
HEADING = "#000"
CAPTION = "#7A7A7A"
SLATE_BORDER = "#E8ECF0"

FONT_BODY = "PingFangSC-light,'PingFang SC','Noto Sans SC','Microsoft YaHei',-apple-system,sans-serif"
FONT_OPTIMA = "Optima-Regular,'Optima','PingFangTC-light','PingFang TC',Georgia,serif"

# --- Style fragments ---
P_STYLE = (f"text-align:justify;font-size:15px;font-family:{FONT_BODY};"
           f"line-height:2;padding:0 8px;color:{TEXT};box-sizing:border-box;"
           f"max-width:640px;margin:0 auto;")

H2_NUM_STYLE = (f"text-align:unset;line-height:0;padding:0 8px;box-sizing:border-box;"
                f"max-width:640px;margin:48px auto 0;")
H2_TITLE_STYLE = (f"text-align:left;font-size:30px;font-family:{FONT_BODY};"
                  f"padding:0 8px;box-sizing:border-box;margin:0 auto 32px;"
                  f"max-width:640px;line-height:1.4;")

H3_STYLE = (f"text-align:left;font-size:17px;font-family:{FONT_BODY};padding:0 8px;"
            f"margin:24px auto 12px;color:{HEADING};line-height:1.6;max-width:640px;")

# H3 with pill (used for sub-sections like L0, 阿里 etc)
PILL_STYLE = (f"display:flex;flex-flow:row;align-items:center;padding:0 8px;"
              f"margin:32px auto 12px;box-sizing:border-box;max-width:640px;")

DIVIDER_BIG = (f'<section style="max-width:640px;margin:32px auto 0;padding:0 8px;">'
               f'<section style="background-color:{CREAM};height:1px;'
               f'box-sizing:border-box;max-width:100%;"><br></section></section>')

DIVIDER_SOFT = (f'<section style="max-width:640px;margin:24px auto;padding:0 8px;">'
                f'<section style="background-color:{CREAM};height:1px;'
                f'box-sizing:border-box;max-width:100%;"><br></section></section>')

BLANK = '<p style="margin:0;"><br></p>'


def render_bold(text, color=None):
    """Convert **bold** to <strong>. Defaults to purple (theme accent).
    Pass color=HEADING (#000) when rendering inside containers that already use
    purple as a structural color (aside titles, core-thesis box) to keep
    visual hierarchy from collapsing."""
    if color is None:
        color = PURPLE
    return re.sub(r'\*\*(.+?)\*\*',
                  lambda m: f'<strong style="font-weight:600;color:{color};">{m.group(1)}</strong>',
                  text)


def is_all_bold(text):
    """Check if the entire paragraph is wrapped in **...** (single span)."""
    text = text.strip()
    if not (text.startswith("**") and text.endswith("**")):
        return False
    inner = text[2:-2]
    return "**" not in inner


def split_first_sentence(text):
    """Split text at first 。？！. Return (first_sentence_incl_punct, rest)."""
    m = re.search(r'([。！？])', text)
    if m:
        end = m.end()
        return text[:end], text[end:]
    return text, ""


def render_paragraph(text, thesis=False):
    """Render a body paragraph. If thesis=True, highlight first sentence."""
    text = text.strip()

    # If the WHOLE paragraph is bold (e.g. **核心论断**), render as #35 Core Thesis Box
    # (visually consistent with #34 Knowledge Aside — rounded lavender container,
    # but no title row; just bold black body as the punch line)
    if is_all_bold(text):
        inner = text[2:-2]
        return (f'<section style="font-size:15px;white-space:normal;margin:20px auto;'
                f'color:{TEXT};font-family:{FONT_BODY};line-height:2;'
                f'background-color:#FAF8FF;border:1px solid {PURPLE};border-radius:8px;'
                f'padding:14px 16px;max-width:640px;box-sizing:border-box;'
                f'text-align:justify;">'
                f'<strong style="font-weight:600;color:{HEADING};">{inner}</strong>'
                f'</section>\n' + BLANK)

    # Otherwise normal paragraph; possibly with thesis highlight on first sentence
    rendered = render_bold(text)
    if thesis:
        first, rest = split_first_sentence(text)
        first_html = f'<span style="background-color:{THESIS_BG};">{render_bold(first)}</span>'
        rest_html = render_bold(rest)
        inner = first_html + rest_html
    else:
        inner = rendered

    return (f'<section style="{P_STYLE}">'
            f'<p style="white-space:normal;margin:0;padding:0;">{inner}</p>'
            f'</section>' + "\n" + BLANK)


def render_h2_mark(number, title):
    """Numbered Section Mark + Title."""
    if number is None:
        # Conclusion / non-numbered: use pill instead
        pill = (f'<section style="display:flex;flex-flow:row;align-items:center;'
                f'padding:0 8px;margin:56px auto 16px;box-sizing:border-box;max-width:640px;">'
                f'<section style="display:inline-block;width:6px;height:24px;'
                f'background-color:{PURPLE};border-radius:30px;flex:0 0 auto;"><br></section>'
                f'<span style="font-family:{FONT_OPTIMA};font-size:16px;color:{PURPLE};'
                f'letter-spacing:2px;margin:0 14px;">EPILOGUE</span>'
                f'<section style="flex:1 1 0%;background-color:#D4D4D4;height:1px;"><br></section>'
                f'</section>')
        title_html = (f'<section style="{H2_TITLE_STYLE}">'
                      f'<p style="margin:0;padding:0;">'
                      f'<strong style="font-weight:600;color:{HEADING};">{title}</strong>'
                      f'</p></section>')
        return pill + "\n" + title_html

    mark = (f'<section style="{H2_NUM_STYLE}">'
            f'<p style="white-space:normal;margin:0;padding:0;">'
            f'<span style="font-size:55px;color:{PURPLE};font-family:{FONT_OPTIMA};">'
            f'<strong>{number:02d}.</strong></span></p>'
            f'<p style="margin:0;padding:0;"><br></p></section>')
    title_html = (f'<section style="{H2_TITLE_STYLE}">'
                  f'<p style="margin:0;padding:0;">'
                  f'<strong style="font-weight:600;color:{HEADING};">{title}</strong>'
                  f'</p></section>')
    return mark + "\n" + title_html


def render_h3(title, use_pill=False, pill_label=""):
    """Render H3 subsection heading. Single-row inline pattern when pill is used.

    Previous 2-row "[pill] ━━━━ / title-below" pattern looked broken when there
    was no label between pill and rule (the gap read as a half-rendered divider).
    New pattern: [pill] [optional label] [title text] all on one row, no trailing
    rule. The pill acts as a left accent marker; the title text carries its own
    weight."""
    if use_pill:
        if pill_label:
            label_html = (f'<span style="font-family:{FONT_OPTIMA};font-size:14px;'
                          f'color:{PURPLE};letter-spacing:1px;font-weight:600;'
                          f'margin:0 10px 0 12px;flex:0 0 auto;">{pill_label}</span>')
        else:
            # No label — small spacer so the title doesn't touch the pill
            label_html = '<span style="display:inline-block;width:12px;flex:0 0 auto;"></span>'
        return (f'<section style="display:flex;flex-flow:row;align-items:center;'
                f'padding:0 8px;margin:32px auto 16px;box-sizing:border-box;'
                f'max-width:640px;">'
                f'<section style="display:inline-block;width:6px;height:20px;'
                f'background-color:{PURPLE};border-radius:30px;flex:0 0 auto;"><br></section>'
                f'{label_html}'
                f'<span style="font-size:17px;font-family:{FONT_BODY};font-weight:600;'
                f'color:{HEADING};line-height:1.5;flex:1 1 0%;">'
                f'{render_bold(title, color=HEADING)}</span>'
                f'</section>')
    else:
        return (f'<section style="{H3_STYLE}">'
                f'<p style="margin:0;padding:0;">'
                f'<strong style="font-weight:600;">{render_bold(title, color=HEADING)}</strong>'
                f'</p></section>')


def render_aside(title, body_items):
    """#34 Cosmic Lavender Knowledge Aside.

    body_items is a list where each entry is either:
      - a string  → a content line (will be separated from the next line by <br/>)
      - None      → a blank line (adds an extra <br/> for paragraph break)

    Every markdown line in the body becomes a rendered line. Blank lines add
    paragraph spacing. No artificial line-count limit. **bold** inside body
    stays black (HEADING) so it doesn't compete with the purple title."""
    parts = []
    prev_blank = False
    last_was_content = False
    for item in body_items:
        if item is None:
            if last_was_content:
                prev_blank = True
            continue
        rendered = render_bold(item, color=HEADING)
        if last_was_content:
            parts.append("<br/><br/>" if prev_blank else "<br/>")
        parts.append(f'<span>{rendered}</span>')
        last_was_content = True
        prev_blank = False
    body_html = "".join(parts)
    return (f'<section style="font-size:15px;white-space:normal;margin:20px auto;'
            f'color:{TEXT};font-family:{FONT_BODY};line-height:2;'
            f'background-color:#FAF8FF;border:1px solid {PURPLE};border-radius:8px;'
            f'padding:14px 16px;max-width:640px;box-sizing:border-box;">'
            f'<strong style="word-break:break-all;font-weight:600;color:{PURPLE};'
            f'font-size:16px;"><span>{title}</span></strong>'
            f'<span><br/><br/></span>{body_html}</section>\n' + BLANK)


def render_reading_card(image_url, title, article_url):
    """One #36 Reading Card: top banner image + bottom title row with lavender chevron.

    WeChat editor quirk: when it sees an `<img>` directly under a block, it
    auto-wraps the image in a `<p>` and inherits the editor's default paragraph
    margins (~32px top + bottom), producing a huge gap between image and title.

    Fix: wrap the image in a `<section>` with `font-size:0;line-height:0;margin:0`
    to suppress paragraph auto-insertion, and set `vertical-align:bottom` on the
    `<img>` to kill the residual inline-baseline gap. The outer card also
    declares `font-size:0;line-height:0` so any stray whitespace nodes between
    children collapse — the title row then re-declares its own font-size."""
    if image_url and image_url not in ("placeholder", "_", "-"):
        img_inner = (f'<img src="{image_url}" alt="" '
                     f'style="display:block;width:100%;margin:0;padding:0;border:0;'
                     f'vertical-align:bottom;" />')
    else:
        img_inner = (f'<section style="width:100%;height:140px;margin:0;padding:0;'
                     f'background:linear-gradient(135deg,#FAF8FF 0%,#E8E4FF 50%,#F5F2FF 100%);'
                     f'display:flex;align-items:center;justify-content:center;">'
                     f'<span style="font-family:{FONT_OPTIMA};font-size:13px;color:{PURPLE};'
                     f'letter-spacing:3px;font-weight:600;opacity:0.7;">COVER · 封面图</span>'
                     f'</section>')

    is_wechat = article_url and "mp.weixin.qq.com" in article_url
    link_open = f'<a href="{article_url}" style="text-decoration:none;color:inherit;display:block;">' if is_wechat else ""
    link_close = "</a>" if is_wechat else ""

    return (
        f'{link_open}'
        f'<section style="border:1px solid {SLATE_BORDER};border-radius:10px;'
        f'overflow:hidden;margin:0 auto 16px;background:#FFFFFF;max-width:640px;'
        f'box-sizing:border-box;font-size:0;line-height:0;">'
        f'<section style="margin:0;padding:0;font-size:0;line-height:0;">'
        f'{img_inner}'
        f'</section>'
        f'<section style="display:flex;align-items:center;justify-content:space-between;'
        f'padding:14px 16px;margin:0;font-size:15px;line-height:1.5;">'
        f'<span style="font-family:{FONT_BODY};color:{TEXT};flex:1 1 0%;font-size:15px;'
        f'line-height:1.5;">{title}</span>'
        f'<span style="display:inline-block;width:24px;height:24px;border-radius:12px;'
        f'background-color:rgba(121,115,247,0.10);text-align:center;line-height:24px;'
        f'color:{PURPLE};font-size:14px;margin-left:12px;flex:0 0 auto;'
        f'font-family:Georgia,serif;font-weight:600;">›</span>'
        f'</section>'
        f'</section>'
        f'{link_close}'
    )


def render_reading(items, header=""):
    """#36 Reading Recommendations section. items: list of (image, title, url) triples.
    Optional header rendered as #26 Purple Pill + Rule with Optima label."""
    parts = []
    if header:
        parts.append(
            f'<section style="display:flex;flex-flow:row;align-items:center;padding:0 8px;'
            f'margin:48px auto 20px;box-sizing:border-box;max-width:640px;">'
            f'<section style="display:inline-block;width:6px;height:22px;'
            f'background-color:{PURPLE};border-radius:30px;flex:0 0 auto;"><br></section>'
            f'<span style="font-family:{FONT_OPTIMA};font-size:15px;color:{PURPLE};'
            f'letter-spacing:2px;font-weight:600;margin:0 14px;">{header}</span>'
            f'<section style="flex:1 1 0%;background-color:#D4D4D4;height:1px;"><br></section>'
            f'</section>'
        )
    parts.append('<section style="max-width:640px;margin:0 auto;padding:0 8px;box-sizing:border-box;">')
    for img, title, url in items:
        parts.append(render_reading_card(img, title, url))
    parts.append('</section>')
    parts.append(BLANK)
    return "\n".join(parts)


def render_task_list(lines):
    """Render the task list as a left-rail purple quote box.
    Spacing aligned with #34 Aside (2026-05): 8px radius, 14px/16px padding,
    20px vertical margin. Keeps its distinct identity via the purple left rail
    + slate 3-side border + white bg, but rhythm matches the aside family."""
    items_html = "<br>".join(f'<span leaf="">{line}</span>' for line in lines)
    return (f'<section style="border:1px solid {SLATE_BORDER};border-left:6px solid {PURPLE};'
            f'border-radius:8px;'
            f'padding:14px 16px;margin:20px auto;background:#FFFFFF;box-sizing:border-box;'
            f'max-width:640px;">'
            f'<p style="white-space:normal;margin:0;padding:0;font-size:15px;'
            f'font-family:{FONT_BODY};line-height:2;color:{TEXT};">{items_html}</p>'
            f'</section>\n' + BLANK)


def main():
    with open(MD_PATH, encoding="utf-8") as f:
        md = f.read()

    lines = md.split("\n")

    # Walk and parse
    out = []
    out.append('<section style="background:#FFFFFF;padding:0;">')

    # State
    h2_counter = 0
    in_section = False  # Are we inside an H2 (so we know when to apply thesis)
    expect_thesis = False

    # We need to know if H3 is inside section 四 or 五 (uses pill style)
    # Section 四 H3s: L0, L1, ... → pill with label
    # Section 五 H3s: 阿里, 京东, etc → pill without label (or with short label)
    section_uses_pill_h3 = False
    pill_label_provider = None

    # Section title → behavior tag
    SECTION_H3_BEHAVIOR = {
        "下一代商业价值链，会被重新拆层": "pill_label",  # use L0/L1 labels from heading text
        "主要玩家会被重新摆位": "pill_plain",
    }

    # Collect task list block (lines 101-105 in source)
    pending_task_lines = []

    i = 0
    n = len(lines)
    first_h2_seen = False
    current_h2_for_h3 = None

    while i < n:
        line = lines[i].rstrip()
        stripped = line.strip()

        # H1
        if stripped.startswith("# ") and not stripped.startswith("## "):
            title = stripped[2:].strip()
            out.append(f'<section style="max-width:640px;margin:0 auto;'
                       f'padding:32px 8px 8px;box-sizing:border-box;">'
                       f'<h1 style="font-family:{FONT_BODY};font-size:28px;font-weight:600;'
                       f'color:{HEADING};line-height:1.5;margin:0;text-align:left;'
                       f'word-break:break-all;">{title}</h1></section>')
            i += 1
            continue

        # Byline (line right after H1: "作者：...")
        if stripped.startswith("作者：") and not in_section:
            byline = stripped
            out.append(f'<section style="text-align:left;font-size:15px;'
                       f'font-family:{FONT_OPTIMA};line-height:2;padding:0 8px;'
                       f'margin:16px auto 8px;color:{CAPTION};box-sizing:border-box;'
                       f'max-width:640px;"><p style="white-space:normal;margin:0;padding:0;">'
                       f'<span leaf="">{byline}</span></p></section>')
            i += 1
            continue

        # Reading-recommendations fence (:::reading ... :::)
        # Each card is 3 consecutive non-blank lines: image_url / title / article_url
        # Blank lines separate cards. Optional header after `:::reading `.
        if stripped == ":::reading" or stripped.startswith(":::reading "):
            header = stripped[len(":::reading"):].strip()
            j = i + 1
            block = []
            while j < n and lines[j].strip() != ":::":
                block.append(lines[j].rstrip())
                j += 1
            items = []
            current = []
            for ln in block:
                s = ln.strip()
                if s == "":
                    if len(current) == 3:
                        items.append(tuple(current))
                    current = []
                else:
                    current.append(s)
            if len(current) == 3:
                items.append(tuple(current))
            out.append(render_reading(items, header))
            i = j + 1
            expect_thesis = False
            continue

        # Aside fence (:::aside ... :::)
        # No line-count limit. Each markdown line in the body becomes a
        # rendered line (separated by <br/> from the next). Blank lines add a
        # paragraph break (extra <br/> for breathing room). The author has full
        # control over whether the aside is 1 line, 3 paragraphs, or 20 rows.
        if stripped == ":::aside":
            j = i + 1
            block = []
            while j < n and lines[j].strip() != ":::":
                block.append(lines[j])
                j += 1
            title = ""
            body_items = []  # list of str (content line) or None (blank line)
            title_set = False
            for ln in block:
                s = ln.strip()
                if not title_set:
                    if s:
                        title = s
                        title_set = True
                    continue
                if s == "":
                    body_items.append(None)
                else:
                    body_items.append(s)
            # Trim leading/trailing blanks within body
            while body_items and body_items[0] is None:
                body_items.pop(0)
            while body_items and body_items[-1] is None:
                body_items.pop()
            out.append(render_aside(title, body_items))
            i = j + 1
            expect_thesis = False
            continue

        # Divider
        if stripped == "---":
            out.append(DIVIDER_SOFT)
            i += 1
            continue

        # H2
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            # Strip "一、" "二、" etc.
            cleaned = re.sub(r'^[一二三四五六七八九十百千]+、', '', title)
            cleaned = re.sub(r'^结语[：:]?\s*', '', title) if title.startswith("结语") else cleaned

            number = None
            # Note: we DO NOT auto-emit a divider before H2 — the markdown source
            # already places explicit `---` between sections, and the H2 mark's
            # own 48px top margin provides the breathing room. Auto-adding a
            # divider here would stack a second hairline on top of the one
            # already rendered from `---`, producing visible double lines.
            if title.startswith("结语"):
                # Use EPILOGUE pill, keep title text after "结语："
                m = re.match(r'^结语[：:]?\s*(.*)$', title)
                clean_title = m.group(1) if m else title
                out.append(render_h2_mark(None, clean_title))
            elif cleaned in NO_NUMBER_HEADINGS:
                out.append(render_h2_mark(None, cleaned))
            else:
                h2_counter += 1
                out.append(render_h2_mark(h2_counter, cleaned))

            in_section = True
            expect_thesis = True
            current_h2_for_h3 = cleaned if cleaned not in NO_NUMBER_HEADINGS and not title.startswith("结语") else cleaned
            i += 1
            continue

        # H3
        if stripped.startswith("### "):
            title = stripped[4:].strip()

            behavior = SECTION_H3_BEHAVIOR.get(current_h2_for_h3, "plain")
            if behavior == "pill_label":
                # L0：协议与授权层 → label="L0", title="协议与授权层"
                m = re.match(r'^(L\d+)[：:]\s*(.*)$', title)
                if m:
                    out.append(render_h3(m.group(2), use_pill=True, pill_label=m.group(1)))
                else:
                    out.append(render_h3(title, use_pill=True))
            elif behavior == "pill_plain":
                # 阿里：从流量平台...  → no label, replace ：with ·
                new_title = title.replace("：", " · ")
                out.append(render_h3(new_title, use_pill=True))
            else:
                # 写在前面, 先说结论 → plain H3
                out.append(render_h3(title))
            expect_thesis = False  # H3 resets - don't put thesis on next para
            i += 1
            continue

        # Task list (5 lines starting with curly quote "), each ending with " (curly)
        if stripped.startswith("“") and stripped.endswith("”"):
            block = []
            j = i
            while j < n:
                s = lines[j].strip()
                if s.startswith("“") and s.endswith("”"):
                    block.append(s)
                    j += 1
                elif s == "":
                    break
                else:
                    break
            if len(block) >= 2:
                out.append(render_task_list(block))
                i = j
                continue

        # Empty line
        if stripped == "":
            i += 1
            continue

        # Default: paragraph
        out.append(render_paragraph(stripped, thesis=expect_thesis))
        if expect_thesis:
            expect_thesis = False
        i += 1

    out.append(f'<section style="max-width:640px;margin:32px auto;padding:0 8px;">'
               f'<section style="background-color:{CREAM};height:1px;'
               f'box-sizing:border-box;max-width:100%;"><br></section></section>')
    out.append(f'<section style="text-align:center;font-size:13px;'
               f'font-family:{FONT_OPTIMA};line-height:2;padding:0 8px;'
               f'margin:16px auto 32px;color:{CAPTION};box-sizing:border-box;'
               f'max-width:640px;"><p style="white-space:normal;margin:0;padding:0;">'
               f'<span leaf="">— Arron Young —</span></p></section>')
    out.append('</section>')

    html = "\n".join(out)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)

    # Build preview
    with open(TEMPLATE, encoding="utf-8") as f:
        tmpl = f.read()
    preview = tmpl.replace("<!-- ARTICLE_CONTENT_PLACEHOLDER -->", html)
    preview = preview.replace(
        "<h1>WeChat Preview</h1>",
        "<h1>离开京东后，我重新理解了 AI 时代电商的第一性原理（最终版）</h1>"
    )
    preview = preview.replace(
        '<span class="theme-tag" id="theme-tag"></span>',
        f'<span class="theme-tag" id="theme-tag" style="background:{PURPLE};color:#fff;">寰宇紫 Cosmic Lavender</span>'
    )
    with open(PREVIEW_PATH, "w", encoding="utf-8") as f:
        f.write(preview)

    # Stats
    text = re.sub(r'<[^>]+>', '', html)
    text = re.sub(r'\s', '', text)
    print(f"chars: {len(text)}")
    print(f"reading time: {(len(text) + 299) // 300} min")
    print(f"article: {OUT_PATH}")
    print(f"preview: {PREVIEW_PATH}")


if __name__ == "__main__":
    main()
