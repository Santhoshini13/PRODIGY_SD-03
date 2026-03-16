contacts = {}
while True:
    print("\nContact Management System")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print("Contact added successfully!")
    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            for name, info in contacts.items():
                print(f"\nName: {name}")
                print("Phone:", info["Phone"])
                print("Phone:", info["Phone"])
    elif choice == "3":
        name = input ("Enter contact name to edit: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            contacts[name] = {"phone": phone, "Email": email}
            print("Contact updated!")
        else:
            print("Contact not found")
    elif choice == "4":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("Contact not found")
    elif choice == "5":
        print("Existing program")
        break
    else:
        print("Invalid choice Try again")
        
