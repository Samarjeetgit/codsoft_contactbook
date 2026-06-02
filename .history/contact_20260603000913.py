import json
import os

def load_data():
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as f:
            return json.load(f)
    return {}

def save_data(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f, indent=2)

def show_menu():
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")
    return input("Action: ")

def main():
    contacts = load_data()
    
    while True:
        choice = show_menu()
        
        if choice == '1':
            name = input("Name: ").strip()
            if name in contacts:
                print("Contact already exists.")
                continue
            contacts[name] = {
                "phone": input("Phone: ").strip(),
                "email": input("Email: ").strip(),
                "address": input("Address: ").strip()
            }
            save_data(contacts)
            print("Done.")

        elif choice == '2':
            if not contacts:
                print("List is empty.")
            for name, info in contacts.items():
                print(f"{name.ljust(15)} | {info['phone']}")

        elif choice == '3':
            query = input("Search name/phone: ").lower()
            found = False
            for name, info in contacts.items():
                if query in name.lower() or query in info['phone']:
                    print(f"\n[{name}]\nPh: {info['phone']}\nEm: {info['email']}\nAd: {info['address']}")
                    found = True
            if not found: print("No match.")

        elif choice == '4':
            name = input("Target Name: ").strip()
            if name in contacts:
                print("Enter new values (leave blank to skip)")
                contacts[name]["phone"] = input(f"Phone [{contacts[name]['phone']}]: ") or contacts[name]["phone"]
                contacts[name]["email"] = input(f"Email [{contacts[name]['email']}]: ") or contacts[name]["email"]
                contacts[name]["address"] = input(f"Address [{contacts[name]['address']}]: ") or contacts[name]["address"]
                save_data(contacts)
                print("Updated.")
            else:
                print("Not found.")

        elif choice == '5':
            name = input("Delete Name: ").strip()
            if name in contacts:
                del contacts[name]
                save_data(contacts)
                print("Deleted.")
            else:
                print("Not found.")

        elif choice == '6':
            print("Closing...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()1