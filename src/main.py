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

#  ========== Patterns for extractions ==============

email_pattern = re.compile(r"\b[a-zA-Z0-9\-._+%]+@[a-zA-Z0-9\.\-]+\.[a-z]{2,}\b", re.I)  #Username:letters, digits,dot, hyphen or _ @ domain: letters, -, .

phone_pattern = re.compile(r"\(?(?:\b|\+)\d{1,3}\)?[\s-]\(?\d{2,4}\)?[-\s]?\d{2,4}[-\s]?\d{2,4}\b") #lengths 7 to 15, +(optional), countrycode, separators: whitespace, -, (), or no separator

Time = re.compile(r"\b(?:[0-1]\d|2[0-3]):[0-5]\d\b")  #Matches valid 24-h format: from 00:00 to 23:59. Hours: 00 to 23; Minutes: from 00-59.

Card = re.compile(r"\b(\d{4}[-\s]?){3}\d{4}\b")  # Matches 16-digit card numbers
#4 groups of 4 digits each, separated by spaces, or hyphens, or nothing.


#Time extraction, format 24-h
for t in Time.finditer(text):
    print(t.group())


#credit card number extraction
for c in Card.finditer(text):
    print(c.group())

#========== Validation functions ===========

#Extra validation of the extracted email
def email_isvalid(email):
    return ( "@" in email
            and not email.startswith("@")
            and not email.endswith("@")
            and ".." not in email
            )

#classify emails according to the ALU domains stipulated. Returns none if not an ALU address.
def alu_email(email):
    if email.endswith("@alueducation.com"):
        return "official"
    if email.endswith("@alumni.alueducation.com"):
        return "alumni"
    if email.endswith("@si.alueducation.com"):
        return "si"
    
    return None

#remove spaces and hyphens for a card number
def normal_card(card):
    return re.sub(r"[-\s]", "", card)

#Validate a card number using the luhn algorithm
def luhn_check(card):
    digits = [int(digit) for digit in card_number]

    checksum = 0
    balance = len(digits) % 2

    for index, digit in enumerate(digits):
        if index % 2 == balance:
            digit *= 2

            if digit > 9:
                digit -= 9
        checksum += digit
    return checksum % 10 == 0

#mask all the digits except the last four digits of a card number.
def mask_card(card):
    return "*" * (len(card)-4) + card[-4:]

# =====Result storage dictionary=====
reuslts = {
        "emails": [],
        "alu_emails": {
        "official": [],
        "alumni": [],
        "si": []
        },
        "phone_numbers": [],
        "times": [],
        "credit_cards":[]
        }
     

# ==== Extraction =====

#emails extraction
for e in email_pattern.finditer(text):
    email = e.group()

    if not email_isvalid(email):
        continue
    results["emails"].append(email)
    alu_type = alu_email(email)

    if alu_type:
        results["alu_emails"][alu_type].append(email)

#phone number extraction.                                                   
for p in phone_pattern.finditer(text):
    phone = p.group()

    results["phone_numbers"].append(phone)

#Time extraction, format 24-h                                               
for t in Time.finditer(text):
    time = t.group()
    results["times"].append(time)

#Credit card extraction
for c in Card.finditer(text):
    card = c.group()

    #remove spaces and hyphens
    normalized_card = normal_card(card)
