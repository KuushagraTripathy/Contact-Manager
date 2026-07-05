contacts = list() # This is used to make a list 
def show_menu(): # This is used to show the menu
    print("=== CONTACT MANAGER ===")
    print("1. Add Contact", "2. View All Contacts", "3. Search Contact", "4. Delete Contact", "5. Exit", sep=("\n"))
def add_contact(): # This is to add a contact to the list
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    personal_information = { #This is a dictionary
        "name": name,
        "phone_number": phone_number,
        "email": email
        }
    contacts.append(personal_information)
    print(f"You have successfully added a contact!", personal_information)
def view_contacts(): # This will view contacts
    if not contacts: # This checks if the list is empty, using 'not'
        print("No contacts found")
    else:
        for contact in contacts: # This is to start the loop
            print(f"Name: {contact["name"]}, Phone: {contact["phone_number"]}, Email: {contact["email"]}")
def search_contact(): # This will help to search for contacts
    search_term = input("Enter name or phone number to search: ").lower()
    found = False
    for contact in contacts:
        if search_term in contact["name"].lower() or search_term in contact["phone_number"]: # Search by name (case insensitive) or phone number
            print(f"\n✅ Contact found!")
            print(f"Name: {contact["name"]}")
            print(f"Phone: {contact["phone_number"]}")
            print(f"Email: {contact["email"]}")
            found = True
        if not found:
            print("\n❌ Contact not found")
def delete_contact(): # This will delete a contact
    erase_contact = input("Enter contact you want to delete: ").lower()
    deleted_contact = False
    for contact in contacts:
        if contact['name'].lower() == erase_contact: # ✅ Check if the name matches
            print("Contact deleted!")
            deleted_contact = True
            contacts.remove(contact)  # Actually removes the contact from the list
            break # ✅ Stop the loop after deleting
    if not deleted_contact:
            print("Contact not found!")
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")