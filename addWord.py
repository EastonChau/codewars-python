#!/usr/bin/env python3
# This programme stores the first argument in the terminal in a text file named "vocab.txt"
# nano ~/.zshrc :chmod +x [working directory (need to edit)]/addWord.py
# alias addw="python3 [working directory (need to edit)]/addWord.py"
# usage: addw apple

import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("argument lacked")
    sys.exit(1)

file = Path("vocab.txt")

file.touch()

content = file.read_text(encoding="utf-8").strip()

words = [word.strip() for word in content.split(",")]

words.append(sys.argv[1])

file.write_text(",".join(words), encoding="utf-8")