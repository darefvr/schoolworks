import pymongo
from pymongo import MongoClient

# Connect to the local MongoDB instance
client = MongoClient('mongodb://localhost:27017/')
database_name = 'mydatabase'
collection_name = 'mycollection'
db = client[database_name]
collection = db[collection_name]

def create_document():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    email = input("Enter email: ")

    document = {
        "name": name,
        "age": age,
        "email": email
    }

    result = collection.insert_one(document)
    print(f"Document with ID {result.inserted_id} created.")

def read_documents():
    documents = collection.find()
    print("All Documents:")
    for document in documents:
        print(document)

def update_document():
    filter_criteria = {"name": input("Enter the name of the document to update: ")}
    update_values = {"$set": {"age": int(input("Enter the new age: "))}}

    result = collection.update_one(filter_criteria, update_values)
    print(f"Matched {result.matched_count} document and modified {result.modified_count} document.")

def delete_document():
    filter_criteria = {"name": input("Enter the name of the document to delete: ")}

    result = collection.delete_one(filter_criteria)
    print(f"Deleted {result.deleted_count} document.")

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Create Document")
        print("2. Read Documents")
        print("3. Update Document")
        print("4. Delete Document")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_document()
        elif choice == "2":
            read_documents()
        elif choice == "3":
            update_document()
        elif choice == "4":
            delete_document()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
