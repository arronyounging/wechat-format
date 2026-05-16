#!/bin/bash
# wechat-format skill installer for Claude Code
# Usage: curl -fsSL https://raw.githubusercontent.com/ArroyYoung/wechat-format/main/install.sh | bash

set -e

SKILL_DIR="$HOME/.claude/skills/wechat-format"

if [ -d "$SKILL_DIR" ]; then
  echo "Updating existing installation at $SKILL_DIR..."
  rm -rf "$SKILL_DIR"
fi

echo "Installing wechat-format skill..."
mkdir -p "$HOME/.claude/skills"
git clone --depth 1 https://github.com/ArroyYoung/wechat-format.git "$SKILL_DIR"
rm -rf "$SKILL_DIR/.git"

echo ""
echo "Done! wechat-format skill installed at $SKILL_DIR"
echo ""
echo "Usage in Claude Code:"
echo "  /wechat-format your-article.md"
echo "  /wechat-format your-article.md --theme neondusk"
echo ""
