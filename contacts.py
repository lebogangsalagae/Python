#Programme for contacts
#Lebogang Salagae
#11 May 2024

import os

def path_exists(file_path):
    return os.path.exists(file_path)

def add_contact(file_path, name, phone, email):
    if not path_exists(file_path):
        print("Contacts file does not exist.")
        return
    
    # checking if the contact already exists
    with open(file_path, 'r') as file:
        for line in file:
            if name.lower() in line.lower():
                print("Contact already exists.")
                return ""
    
    # adding the contact if it doesn't exist
    with open(file_path, 'a') as file:
        file.write(f"{name} | {phone} | {email}\n")
    print("Contact added successfully.\n")

def custom_sort(contacts):
    return sorted(contacts)

def binary_search(values, query, start, stop):
    if start > stop:
        return -1
   
    middle = (start + stop) // 2
    name_middle = values[middle].split(" | ")[0].lower()
   
    if query.lower() == name_middle:
        return middle
   
    if query.lower() > name_middle:
        return binary_search(values, query, middle + 1, stop)
   
    return binary_search(values, query, start, middle - 1)

def search_contact(file_path, query):
    matching_contacts = []
    with open(file_path, 'r') as file:
        contacts = [line.strip() for line in file]
        sorted_contacts = custom_sort(contacts)  

        index = binary_search(sorted_contacts, query, 0, len(sorted_contacts) - 1)
        if index != -1:
            matching_contacts.append(sorted_contacts[index])
        else:
            for contact in sorted_contacts:
                name, phone, email = contact.split(" | ")
                if len(contact_info) == 3:
                    name, phone, email = contact_info                
                if query.lower() in name.lower() or query.lower() in phone.lower() or query.lower() in email.lower():
                    matching_contacts.append(contact)

            if matching_contacts:
                return matching_contacts
            else:
                print("No contact found.")

    return matching_contacts

def read_contacts(file_path):
    if not path_exists(file_path):
        print("Contacts file does not exist.")
        return []
    
    contacts = []
    with open(file_path, 'r') as file:
        for line in file:
            contact_info = line.strip().split(",")
            contacts.append(contact_info)
    return contacts

def list_contacts(file_path):
    if not path_exists(file_path):
        print("Contacts file does not exist.")
        return
    
    contacts = read_contacts(file_path)
    print("List of contacts:")
    print("=" * 60)
    print("| {:<20} | {:<12} | {:<20} |".format("Name", "Phone", "Email"))
    print("=" * 60)
    for contact in contacts:
        name, phone, email = contact.split(" | ")
        print("| {:<20} | {:<12} | {:<20} |".format(name, phone, email))
        print("-" * 60)

def main():
    file_name = input("Enter the name for the contacts file:\n") + ".txt"
    
    if not path_exists(file_name):
        with open(file_name, 'w'):
            pass
        print(f"Contacts file '{file_name}' created.\n")
    else:
        print("")
    while True:
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. List Contacts")
        print("4. Exit")
        user = input("Enter your choice: ")
        if user == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(file_name, name, phone_number, email)
        elif user == '2':
            query = input("Enter first name, last name, phone number, or email to search:\n")
            found_contacts = search_contact(file_name, query)
            if found_contacts:
                print("Found contact(s):")
                print("=" * 60)
                print("| {:<20} | {:<12} | {:<20} |".format("Name", "Phone", "Email"))
                print("=" * 60)
                for contact in found_contacts:
                    name, phone_number, email = contact.split(" | ")
                    print("| {:<20} | {:<12} | {:<20} |".format(name, phone_number, email))
                    print("-" * 60)
            else:
                print("No contact found.")
        elif user == '3':
            list_contacts(file_name)
        elif user == '4':
            print("Exiting program.")
            break

if __name__ == '__main__':
    main()