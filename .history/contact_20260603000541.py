import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class ContactBook:
    def __init__(self):
        # Store name, phone, email, and address [cite: 67]
        self.contacts = {}

    def add_contact(self):
        print("\n--- Add New Contact ---")
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()
        address = input("Enter Address: ").strip()
        
        if name in self.contacts:
            print(f"Contact '{name}' already exists.")
        else:
            self.contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact added successfully!")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts found.")
        else:
            # Display name and phone numbers [cite: 69]
            for name, details in self.contacts.items():
                print(f"Name: {name} | Phone: {details['phone']}")

    def search_contact(self):
        print("\n--- Search Contact ---")
        query = input("Enter Name or Phone Number to search: ").strip()
        found = False
        # Implement search by name or phone [cite: 70]
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query == details['phone']:
                print(f"\nFound: {name}")
                print(f"Phone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                found = True
        if not found:
            print("No matching contact found.")

    def update_contact(self):
        print("\n--- Update Contact ---")
        name = input("Enter the Name of the contact to update: ").strip()
        if name in self.contacts:
            print("Leave blank to keep current information.")
            phone = input(f"New Phone ({self.contacts[name]['phone']}): ") or self.contacts[name]['phone']
            email = input(f"New Email ({self.contacts[name]['email']}): ") or self.contacts[name]['email']
            address = input(f"New Address ({self.contacts[name]['address']}): ") or self.contacts[name]['address']
            
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            print("Contact updated successfully!") [cite: 71]
        else:
            print("Contact not found.")

    def delete_contact(self):
        print("\n--- Delete Contact ---")
        name = input("Enter the Name of the contact to delete: ").strip()
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!") [cite: 72]
        else:
            print("Contact not found.")

def main():
    book = ContactBook()
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")
        
        if choice == '1': book.add_contact()
        elif choice == '2': book.view_contacts()
        elif choice == '3': book.search_contact()
        elif choice == '4': book.update_contact()
        elif choice == '5': book.delete_contact()
        elif choice == '6': 
            print("Exiting... Good luck with your CodSoft internship!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()