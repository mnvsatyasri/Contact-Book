import csv

file_name = "Contacts.csv"

def add_contact(name,phone):
    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name,phone])
    print("Contact added!")

def view_contacts():
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            print("\n--- Contact List ---")
            for row in reader:
                print(f"Name: {row[0]}, Phone: {row[1]}")
    except FileNotFoundError:
        print("No contacts saved yet.")

def seaarch_contact(name):
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                if row[0].lower() == name.lower():
                    print(f"Found: {row[0]} - {row[1]}")
                    found = True
            if not found:
                print("Contact not found")
    except FileNotFoundError:
        print("No contacts saved yet")

while True:
    print("\nContact Book")
    print("1.Add Contacts")
    print("2.View Contacts")
    print("3.Search Contacts")
    print("4.Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name,phone)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        name = input("Enter name to search: ")
        seaarch_contact(name)
    elif choice == "4":
        print("GoodBye!")
        break
    else:
        print("Invalid choice, try again")
