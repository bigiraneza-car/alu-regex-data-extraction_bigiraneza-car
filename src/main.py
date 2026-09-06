#!/usr/bin/env python3
#importing python's regex module
import re
from pathlib import Path
#Use python's built-in variable to locate the project root for the program to work.
ROOT = Path(__file__).resolve().parent.parent
Input_file = ROOT / "input" / "raw-text.txt"
#Take the entire raw_text as a single string, with utf-8 to read the non_ASCII characters.
text =Input_file.read_text(encoding="utf-8")
#treats the input as untrustworthy
#verify the sucess of the text load in the source code. 
print(f"what is the length of the input text: {len(text)}")
#extraction of the phone numbers, time in 24-h format, emails, and credit card.
#phone number extraction
for phone in re.findall(r"\(?(?:\b|\+)\d{1,3}\)?[\s-]\(?\d{2,4}\)?[-\s]?\d{2,4}[-\s]?\d{2,4}\b", text):
    print(phone)
