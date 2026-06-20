#!/usr/bin/env python3
"""
记录文件编辑历史
在每次 Edit 或 Write 工具调用后运行
"""

import sys
import os
from pathlib import Path

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
    max_history = 50

    # 追加编辑记录
    with open(history_file, "a", encoding="utf-8") as f:
        f.write(file_path + "\n")

    # 保留最近的记录，删除旧记录
    if history_file.exists():
        lines = history_file.read_text(encoding="utf-8").splitlines()
        if len(lines) > max_history:
            with open(history_file, "w", encoding="utf-8") as f:
                f.write("\n".join(lines[-max_history:]) + "\n")

    sys.exit(0)

if __name__ == "__main__":
    main()
