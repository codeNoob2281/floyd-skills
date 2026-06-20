#!/usr/bin/env python3
"""
检查同一文件是否已被连续编辑多次
如果达到阈值，返回非零退出码以拦截操作
"""

import sys
import os
from pathlib import Path

max_edits = 30

def main():
    import json

    try:
        data = json.load(sys.stdin)
        file_path = data.get("tool_input", {}).get("file_path", "")
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    if not file_path:
        sys.exit(0)
    script_dir = Path(__file__).parent
    history_file = script_dir / ".edit-history"

    if not history_file.exists():
        sys.exit(0)

    # 读取历史记录，计算连续编辑次数
    current_count = 0
    with open(history_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == file_path:
                current_count += 1
            else:
                current_count = 0

    # 如果达到阈值，拦截
    if current_count >= max_edits:
        print(f"⚠️ 拦截：文件 '{file_path}' 已被连续编辑 {max_edits} 次。", file=sys.stderr)
        print("请考虑：", file=sys.stderr)
        print("  1. 是否在循环修改同一问题？", file=sys.stderr)
        print("  2. 是否应该一次性完成所有修改？", file=sys.stderr)
        print("  3. 是否需要重新审视修改策略？", file=sys.stderr)
        print("", file=sys.stderr)
        print("如需继续，请先清理编辑历史或等待会话结束。", file=sys.stderr)
        sys.exit(2)

    sys.exit(0)

if __name__ == "__main__":
    main()
