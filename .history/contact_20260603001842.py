```python
import json
import os
import csv
import re

PHONE_PATTERN = r'^\d{10}$'
EMAIL_PATTERN = r'^[\w\.-]+@[\w\.-]+\.\w+$'


def load_data():
    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json", "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Data file corrupted. Starting fresh.")
    return {}


def save_data(contacts):
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=2)


def export_csv(contacts):
    with open("contacts.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email", "Address"])

