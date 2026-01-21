import os

# ---------- Load Contacts ----------
def load_contact(file_name="contact.txt"):
    contact_list = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, phone, email = parts
                    contact_list.append({"name": name, "phone": phone, "email": email})
    else:
        # Create file if it doesn't exist
        with open(file_name, "w") as file:
            pass
    return contact_list

# ---------- Save Contacts ----------
def save_contact(contact_list, file_name="contact.txt"):
    with open(file_name, "w") as file:
        for contact in contact_list:
            line = f"{contact['name']},{contact['phone']},{contact['email']}\n"
            file.write(line)

# ---------- Menu ----------
def show_menu():
    print("\n=== Contact Management System ===")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Search Contacts")
    print("5. Update Contact")
    print("6. Exit")
    print("================================")

# ---------- View Contacts ----------
def view_contacts(contact_list):
    if contact_list:
        print("\nYour Contacts:")
        print("-"*40)
        for i, contact in enumerate(contact_list, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print("-"*40)
    else:
        print("\nNo contacts found.")

# ---------- Add Contact ----------
def add_contact(contact_list):
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    contact_list.append({"name": name, "phone": phone, "email": email})
    save_contact(contact_list)
    print(f"Contact {name} added successfully.")

# ---------- Delete Contact ----------
def delete_contact(contact_list):
    name = input("Enter the name of the contact to delete: ").strip()
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            contact_list.remove(contact)
            save_contact(contact_list)
            print(f"Contact {name} deleted successfully.")
            return
    print(f"Contact {name} not found.")

# ---------- Update Contact ----------
def update_contact(contact_list):
    name = input("Enter the name of the contact to update: ").strip()
    for contact in contact_list:
        if contact['name'].lower() == name.lower():
            new_phone = input("Enter new phone number: ").strip()
            new_email = input("Enter new email address: ").strip()
            contact['phone'] = new_phone
            contact['email'] = new_email
            save_contact(contact_list)
            print(f"Contact {name} updated successfully.")
            return
    print(f"Contact {name} not found.")

# ---------- Search Contacts ----------
def search_contacts(contact_list):
    name = input("Enter the name of the contact to search: ").strip()
    found_contacts = [contact for contact in contact_list if contact['name'].lower() == name.lower()]
    if found_contacts:
        print("\nSearch Results:")
        print("-"*40)
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print("-"*40)
    else:
        print(f"Contact {name} not found.")

# ---------- Main Program ----------
def main():
    contact_list = load_contact()
    
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            view_contacts(contact_list)
        elif choice == "2":
            add_contact(contact_list)
        elif choice == "3":
            delete_contact(contact_list)
        elif choice == "4":
            search_contacts(contact_list)
        elif choice == "5":
            update_contact(contact_list)
        elif choice == "6":
            save_contact(contact_list)
            print("Contacts saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
