#!/usr/bin/env python3
#importing python's regex module
import re
from pathlib import Path
#Use python's built-in variable for paths to the input and output files.
ROOT = Path(__file__).resolve().parent.parent
Input_file = ROOT / "input" / "raw-text.txt"
#Read the entire raw_text as a single string.utf-8 to read non-ASCII character.
text =Input_file.read_text(encoding="utf-8")
#treats the input as untrustworthy

#Patterns for extractions
Email = re.compile(r"\b[a-zA-Z0-9\-._+%]+@[a-zA-Z0-9\.\-]+\.com\b", text, re.I)  #Username:letters, digits,dot, hyphen or _ @ domain: letters, -, .

Phone = re.compile(r"\(?(?:\b|\+)\d{1,3}\)?[\s-]\(?\d{2,4}\)?[-\s]?\d{2,4}[-\s]?\d{2,4}\b", text) #lengths 7to15, +(optional), countrycode, separators: whitespace, -, (), or no separator

Time = re.compile(r"\b(?:[0-1]\d|2[0-3]):[0-5]\d\b", text)  #24-h format: 00:00 to 23:59. hour(1):from 0 to 2, 0 to 9. Minutes: from 0 to 5, 0 to 9.

Card:
#phone number extraction.
for phone in re.findall(r"\(?(?:\b|\+)\d{1,3}\)?[\s-]\(?\d{2,4}\)?[-\s]?\d{2,4}[-\s]?\d{2,4}\b", text):
    print(phone)

#Time extraction, format 24-h
for time in re.findall(r"\b(?:[0-1]\d|2[0-3]):[0-5]\d\b", text):
    print(time)

#emails extraction
for email in re.finditer(r"\b[a-zA-Z0-9\-._+%]+@[a-zA-Z0-9\.\-]+\.com\b", text, re.I):
    print(email.group())
