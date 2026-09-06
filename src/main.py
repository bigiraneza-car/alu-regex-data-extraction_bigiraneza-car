#!/usr/bin/env python3
#importing python's regex module
import re
from pathlib import Path
#Determine the project root directory from the location of this script.
ROOT = Path(__file__).resolve().parent.parent

#Locate the raw input file.
input_file = ROOT / "input" / "raw-text.txt"

#Read the entire input as utf-8 text.
#Content is treated as untrusted external data.
text =input_file.read_text(encoding="utf-8")

#Patterns for extractions
Email = re.compile(r"\b[a-zA-Z0-9\-._+%]+@[a-zA-Z0-9\.\-]+\.[a-z]{2,}\b", re.I)  #Username:letters, digits,dot, hyphen or _ @ domain: letters, -, .

Phone = re.compile(r"\(?(?:\b|\+)\d{1,3}\)?[\s-]\(?\d{2,4}\)?[-\s]?\d{2,4}[-\s]?\d{2,4}\b") #lengths 7to15, +(optional), countrycode, separators: whitespace, -, (), or no separator

Time = re.compile(r"\b(?:[0-1]\d|2[0-3]):[0-5]\d\b")  #24-h format: 00:00 to 23:59. hour(1):from 0 to 2, 0 to 9. Minutes: from 0 to 5, 0 to 9.

Card = re.compile(r"\b\d{4}[-\s]?(\d{4,6}[-\s]?){2,3}\b")  # 4 groups of 4 digits each, or 5 or 6.

#phone number extraction.
for p in Phone.finditer(text):
    print(p.group())

#Time extraction, format 24-h
for t in Time.finditer(text):
    print(t.group())

#emails extraction
for e in Email.finditer(text, re.I):
    print(e.group())

#credit card number extraction
for c in Card.finditer(text):
    print(c.group())
