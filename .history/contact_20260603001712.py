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

        for name, info in contacts.items():
            writer.writerow([
                name,
                info["phone"],
                info["email"],
                info["address"]
            ])

    print("Contacts exported to contacts.csv")


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Export to CSV")
    print("7. Exit")
    return input("Choose an option: ")


def main():
    contacts = load_data()

    while True:
        choice = show_menu()

        # ADD CONTACT
        if choice == "1":
            name = input("Name: ").strip().title()

            if name in contacts:
                print("Contact already exists.")
                continue

            phone = input("Phone (10 digits): ").strip()

            if not re.match(PHONE_PATTERN, phone):
                print("Invalid phone number.")
                continue

            duplicate = False
            for info in contacts.values():
                if info["phone"] == phone:
                    duplicate = True
                    break

            if duplicate:
                print("Phone number already exists.")
                continue

            email = input("Email: ").strip()

            if not re.match(EMAIL_PATTERN, email):
                print("Invalid email address.")
                continue

            address = input("Address: ").strip()

            contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }

            save_data(contacts)
            print("Contact added successfully.")

        # VIEW ALL
        elif choice == "2":
            if not contacts:
                print("No contacts found.")
                continue

            print(f"\nTotal Contacts: {len(contacts)}")

            for name in sorted(contacts):
                info = contacts[name]

                print("\n----------------------")
                print(f"Name    : {name}")
                print(f"Phone   : {info['phone']}")
                print(f"Email   : {info['email']}")
                print(f"Address : {info['address']}")

        # SEARCH
        elif choice == "3":
            query = input(
                "Search by name, phone or email: "
            ).lower()

            found = False

            for name, info in contacts.items():
                if (
                    query in name.lower()
                    or query in info["phone"]
                    or query in info["email"].lower()
                ):
                    print("\n----------------------")
                    print(f"Name    : {name}")
                    print(f"Phone   : {info['phone']}")
                    print(f"Email   : {info['email']}")
                    print(f"Address : {info['address']}")
                    found = True

            if not found:
                print("No matching contact found.")

        # UPDATE
        elif choice == "4":
            name = input("Enter contact name: ").strip().title()

            if name not in contacts:
                print("Contact not found.")
                continue

            print("Leave blank to keep old value.")

            phone = input(
                f"Phone [{contacts[name]['phone']}]: "
            ).strip()

            if phone:
                if not re.match(PHONE_PATTERN, phone):
                    print("Invalid phone number.")
                    continue

                duplicate = False

                for n, info in contacts.items():
                    if n != name and info["phone"] == phone:
                        duplicate = True
                        break

                if duplicate:
                    print("Phone number already exists.")
                    continue

                contacts[name]["phone"] = phone

            email = input(
                f"Email [{contacts[name]['email']}]: "
            ).strip()

            if email:
                if not re.match(EMAIL_PATTERN, email):
                    print("Invalid email.")
                    continue

                contacts[name]["email"] = email

            address = input(
                f"Address [{contacts[name]['address']}]: "
            ).strip()

            if address:
                contacts[name]["address"] = address

            save_data(contacts)
            print("Contact updated.")

        # DELETE
        elif choice == "5":
            name = input("Enter name to delete: ").strip().title()

            if name not in contacts:
                print("Contact not found.")
                continue

            confirm = input(
                f"Delete {name}? (Y/N): "
            ).upper()

            if confirm == "Y":
                del contacts[name]
                save_data(contacts)
                print("Contact deleted.")
            else:
                print("Deletion cancelled.")

        # EXPORT CSV
        elif choice == "6":
            export_csv(contacts)

        # EXIT
        elif choice == "7":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
```
