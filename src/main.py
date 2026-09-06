#!/usr/bin/env python3
#importing python's regex module
import re
from pathlib import Path
#Use python's built-in variable to locate the project root for the program to work.
ROOT = Path(__file__).resolve().parent.parent
Input_file = ROOT / "input" / "raw-text.txt"
#Take the entire raw_text as a single string, with utf-8 to read the non_ASCII characters.
text =Input_file.read_text(encoding="utf-8")
