# Contact Book
# Store, search, update, and delete contacts
# Data saved to a local JSON file so it persists between runs

import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def show_all(contacts):
    if not contacts:
        print("\nNo contacts saved yet.\n")
        return
    print(f"\n--- Contacts ({len(contacts)}) ---")
    for i, c in enumerate(contacts, 1):
        print(f"  {i}. {c['name']}  |  {c['phone']}")
    print()

def add_contact(contacts):
    print("\n-- Add New Contact --")
    name = input("Name: ").strip()
    if not name:
        print("Name can't be empty.")
        return

    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()
    address = input("Address (optional): ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(f"Contact '{name}' saved!")

def view_contact(contacts):
    show_all(contacts)
    if not contacts:
        return
    try:
        num = int(input("Enter number to view details: "))
        c = contacts[num - 1]
        print(f"\n  Name:    {c['name']}")
        print(f"  Phone:   {c['phone']}")
        print(f"  Email:   {c['email'] or '—'}")
        print(f"  Address: {c['address'] or '—'}\n")
    except (ValueError, IndexError):
        print("Invalid number.")

def search_contacts(contacts):
    query = input("\nSearch by name or phone: ").strip().lower()
    results = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]
    if not results:
        print("No matches found.")
    else:
        print(f"\n  Found {len(results)} result(s):")
        for c in results:
            print(f"  → {c['name']}  |  {c['phone']}  |  {c['email'] or '—'}")
    print()

def update_contact(contacts):
    show_all(contacts)
    if not contacts:
        return
    try:
        num = int(input("Enter number to update: "))
        c = contacts[num - 1]
        print("Leave blank to keep current value.\n")

        new_name = input(f"Name ({c['name']}): ").strip()
        new_phone = input(f"Phone ({c['phone']}): ").strip()
        new_email = input(f"Email ({c['email'] or 'none'}): ").strip()
        new_address = input(f"Address ({c['address'] or 'none'}): ").strip()

        if new_name:
            c["name"] = new_name
        if new_phone:
            c["phone"] = new_phone
        if new_email:
            c["email"] = new_email
        if new_address:
            c["address"] = new_address

        save_contacts(contacts)
        print("Contact updated!")
    except (ValueError, IndexError):
        print("Invalid number.")

def delete_contact(contacts):
    show_all(contacts)
    if not contacts:
        return
    try:
        num = int(input("Enter number to delete: "))
        removed = contacts.pop(num - 1)
        save_contacts(contacts)
        print(f"Deleted '{removed['name']}'.")
    except (ValueError, IndexError):
        print("Invalid number.")

def main():
    print("=== Contact Book ===")
    contacts = load_contacts()

    menu = {
        "1": ("View all contacts", lambda: show_all(contacts)),
        "2": ("Add contact", lambda: add_contact(contacts)),
        "3": ("View contact details", lambda: view_contact(contacts)),
        "4": ("Search contacts", lambda: search_contacts(contacts)),
        "5": ("Update contact", lambda: update_contact(contacts)),
        "6": ("Delete contact", lambda: delete_contact(contacts)),
        "7": ("Exit", None),
    }

    while True:
        print("1.View  2.Add  3.Details  4.Search  5.Update  6.Delete  7.Exit")
        choice = input("Choose: ").strip()
        if choice == "7":
            print("Bye!")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Pick 1–7.")

if __name__ == "__main__":
    main()
