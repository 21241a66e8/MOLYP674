import csv
import os

class ContactManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.fieldnames = ["Name", "Email", "Phone"]

    def create_csv_file(self):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

    def read_contacts(self):
        contacts = []
        with open(self.file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
        return contacts

    def add_contact(self, contact):
        contacts = self.read_contacts()
        contacts.append(contact)
        self._write_contacts(contacts)

    def update_contact(self, old_contact, new_contact):
        contacts = self.read_contacts()
        if old_contact in contacts:
            index = contacts.index(old_contact)
            contacts[index] = new_contact
            self._write_contacts(contacts)
        else:
            print("Contact not found.")

    def _write_contacts(self, contacts):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(contacts)
file_path = "contacts.csv"
contact_manager = ContactManager(file_path)

# Create the CSV file (run only once)
if not os.path.exists(file_path):
    contact_manager.create_csv_file()

# Add a new contact
new_contact = {"Name": "john", "Email": "john.doe@ex.com", "Phone": "555-1234"}
contact_manager.add_contact(new_contact)

# Update a contact
old_contact = {"Name": "John", "Email": "john.doe@ex.com", "Phone": "555-1234"}
updated_contact = {"Name": "John", "Email": "john.doe@gmail.com", "Phone": "555-5678"}
contact_manager.update_contact(old_contact, updated_contact)

# Read all contacts
all_contacts = contact_manager.read_contacts()
print("All Contacts:")
print(all_contacts)