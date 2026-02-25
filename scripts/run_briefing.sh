#!/bin/bash

# Ecosystem-standard runner for Medical AI Research
# This script can be called by system cron or the agent itself.

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_DIR="/mnt/windows/cml/clawdbot_reports/medical"
TOPICS=("MDT (Multidisciplinary Team)" "Medical Foundation Models" "In-Silico Clinical Trials" "OCR Induced Noise in NLP Tasks")
TODAY=$(date +"%Y-%m-%d")

mkdir -p "$OUTPUT_DIR"

# 标注输出头 (stdout)
echo "# 🏥 医疗 AI 研报播报机器人 (Medical AI Research Briefing Bot)"
echo "**运行日期**: $TODAY"
echo ""

for TOPIC in "${TOPICS[@]}"; do
    FILE_NAME=$(echo "$TOPIC" | tr ' ' '_' | tr -d '()')
    
    # 调试信息写到 stderr，不污染正文
    echo "正在处理研究方向: $TOPIC ..." >&2
    
    echo "## $TOPIC 研报摘要"
    echo "*(请直接在频道中使用 [方向+简报] 获取详细全文)*"
    echo ""
done

echo "---"
echo "*由医疗 AI 研报技能 v0.1.0 自动生成*"
