#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
医疗 AI 研报播报机器人 (Medical AI Research Briefing Bot) - 飞书推送脚本。
参考模式：从标准输入 (stdin) 获取内容并发送至 Webhook信号。
"""

import sys
import json
import urllib.request

def send_feishu(webhook_url, content):
    """向飞书 Webhook 发送 Markdown 消息。"""
    payload = {
        "msg_type": "markdown",
        "markdown": {
            "content": content
        }
    }

    try:
        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"发送至飞书出错: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # 需要传入 Webhook URL 作为第一个参数
    if len(sys.argv) < 2:
        print("用法: python3 feishu_push.py <WEBHOOK_URL>", file=sys.stderr)
        sys.exit(1)
    
    webhook_url = sys.argv[1]
    # 从标准输入读取内容（通常是从 run_briefing.sh 传过来的管道内容）
    content = sys.stdin.read()
    
    if content.strip():
        print(f"收到 {len(content)} 字节内容。正在发送至飞书...", file=sys.stderr)
        result = send_feishu(webhook_url, content)
        if result:
            print("成功发送至飞书。")
    else:
        print("未收到任何输入内容。", file=sys.stderr)
