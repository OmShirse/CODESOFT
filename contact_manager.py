contacts = []

def show_menu():
    print("\n" + "="*60)
    print("                  📞 CONTACT BOOK")
    print("="*60)
    print("1. Add new contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Exit")
    print("="*60)

def add_contact():
    print("\n--- Add New Contact ---")
    
    name = input("Enter name: ").strip()
    if not name:
        print("Name can't be empty!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print(f"\n✅ Contact '{name}' added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("\n📭 No contacts saved yet. Add some contacts first!")
        return
    
    print("\n" + "="*60)
    print("                  ALL CONTACTS")
    print("="*60)
    
    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print(f"   Address: {contact['address']}")
        print("-"*60)

def search_contact():
    if len(contacts) == 0:
        print("\n📭 No contacts to search!")
        return
    
    search_term = input("\nEnter name or phone number to search: ").strip().lower()
    
    found = []
    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone']:
            found.append(contact)
    
    if len(found) == 0:
        print(f"\n❌ No contacts found matching '{search_term}'")
    else:
        print(f"\n🔍 Found {len(found)} contact(s):")
        print("="*60)
        for contact in found:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-"*60)

def update_contact():
    if len(contacts) == 0:
        print("\n📭 No contacts to update!")
        return
    
    search_name = input("\nEnter the name of contact to update: ").strip()
    
    contact_found = None
    for contact in contacts:
        if contact['name'].lower() == search_name.lower():
            contact_found = contact
            break
    
    if not contact_found:
        print(f"\n❌ Contact '{search_name}' not found!")
        return
    
    print("\nCurrent information:")
    print(f"Name: {contact_found['name']}")
    print(f"Phone: {contact_found['phone']}")
    print(f"Email: {contact_found['email']}")
    print(f"Address: {contact_found['address']}")
    
    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    print("4. Address")
    print("5. All details")
    
    choice = input("\nChoose option (1-5): ")
    
    if choice == "1":
        new_name = input("Enter new name: ").strip()
        if new_name:
            contact_found['name'] = new_name
            print("✅ Name updated!")
    
    elif choice == "2":
        new_phone = input("Enter new phone: ").strip()
        contact_found['phone'] = new_phone
        print("✅ Phone updated!")
    
    elif choice == "3":
        new_email = input("Enter new email: ").strip()
        contact_found['email'] = new_email
        print("✅ Email updated!")
    
    elif choice == "4":
        new_address = input("Enter new address: ").strip()
        contact_found['address'] = new_address
        print("✅ Address updated!")
    
    elif choice == "5":
        contact_found['name'] = input("Enter new name: ").strip()
        contact_found['phone'] = input("Enter new phone: ").strip()
        contact_found['email'] = input("Enter new email: ").strip()
        contact_found['address'] = input("Enter new address: ").strip()
        print("✅ All details updated!")
    
    else:
        print("Invalid choice!")

def delete_contact():
    if len(contacts) == 0:
        print("\n📭 No contacts to delete!")
        return
    
    search_name = input("\nEnter the name of contact to delete: ").strip()
    
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == search_name.lower():
           
            confirm = input(f"Are you sure you want to delete '{contact['name']}'? (yes/no): ")
            if confirm.lower() == 'yes' or confirm.lower() == 'y':
                contacts.pop(i)
                print(f"\n✅ Contact '{search_name}' deleted successfully!")
                return
            else:
                print("Deletion cancelled.")
                return
    
    print(f"\n❌ Contact '{search_name}' not found!")

def main():
    print("\n👋 Welcome to Contact Book!")
    print("Keep all your contacts organized in one place")
    
   
    while True:
        show_menu()
        
        choice = input("\nWhat would you like to do? (1-6): ")
        
        if choice == "1":
            add_contact()
        
        elif choice == "2":
            view_contacts()
        
        elif choice == "3":
            search_contact()
        
        elif choice == "4":
            update_contact()
        
        elif choice == "5":
            delete_contact()
        
        elif choice == "6":
            print("\n👋 Goodbye! Your contacts are safe here.")
            break
        
        else:
            print("\n❌ Invalid choice! Please pick a number between 1-6")
        
     
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
