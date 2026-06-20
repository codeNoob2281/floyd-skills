#!/usr/bin/env python3
"""
清理编辑历史临时文件
在会话结束时运行
"""

import sys
import os
from pathlib import Path

def main():
    script_dir = Path(__file__).parent
    history_file = script_dir / ".edit-history"

    if history_file.exists():
        history_file.unlink()

    sys.exit(0)

if __name__ == "__main__":
    main()
