# CodSoft: Contact Book Application

A clean, terminal-based Contact Book application built with Python as part of the CodSoft Python Programming internship. This project implements full CRUD (Create, Read, Update, Delete) operations and uses JSON for persistent data storage, ensuring your contact details are saved even after closing the program.

## Features

- **Add Contact:** Store contact details including Name, Phone Number, Email, and Address.
- **View All Contacts:** Display a formatted list of all saved contacts showing names and phone numbers.
- **Search Contact:** Search for existing contacts instantly by searching for a partial name or full phone number.
- **Update Contact:** Modify existing contact information with an option to keep current details by leaving inputs blank.
- **Delete Contact:** Remove specific contact records from the database permanently.
- **Persistent Storage:** Automatically saves records to a local `contacts.json` file.

## Prerequisites

- Python 3.x installed on your machine.
- No external dependencies or external packages are required (uses built-in `json` and `os` libraries).

## How to Run

1. Clone this repository to your local machine:
```bash
   git clone [https://github.com/Samarjeetgit/codsoft_contactbook.git](https://github.com/Samarjeetgit/codsoft_contactbook.git)
Navigate into the project folder:
cd codsoft_contactbook
Run the application:
python contact_book.py
File Structure
contact_book.py - The main Python script containing the application logic.

contacts.json - Generated automatically upon adding your first contact to persist data.

README.md - Documentation for the project.
License
This project is built for educational and internship evaluation purposes under the CodSoft internship program.
---

### Ready to Update GitHub?
Since your code is already prepared, you can add this `README.md` to your directory and push the updates directly using these commands:

```bash
git add README.md
git commit -m "Docs: Add clean README instructions"
git push origin main
