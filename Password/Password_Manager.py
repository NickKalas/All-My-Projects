import json

# Load credentials from file (if it exists)
try:
    with open("passwords.json", "r") as file:
        credentials = json.load(file)
except FileNotFoundError:
    credentials = []

def save_to_file():
    with open("Password\passwords.json", "w") as file:
        json.dump(credentials, file, indent=4)

def add_credential():
    website = input("🌐 Enter website: ")
    username = input("👤 Enter username: ")
    password = input("🔐 Enter password: ")
    credentials.append({
        "website": website,
        "username": username,
        "password": password
    })
    print("✅ Credential saved!")
    save_to_file()

def view_credentials():
    if not credentials:
        print("😴 No saved credentials yet!")
        return
    print("📋 All saved credentials:")
    print("-" * 40)
    for entry in credentials:
        print(f"🌐 {entry['website']} | 👤 {entry['username']} | 🔐 {entry['password']}")

def search_credential():
    target = input("🔍 Enter website to search: ")
    for entry in credentials:
        if entry["website"].lower() == target.lower():
            print(f"✅ Found: 👤 {entry['username']} | 🔐 {entry['password']}")
            return
    print("❌ No entry found for that website.")

def delete_credential():
    target = input("🗑️ Enter website to delete: ")
    for entry in credentials:
        if entry["website"].lower() == target.lower():
            credentials.remove(entry)
            print("🗑️ Entry deleted.")
            save_to_file()
            return
    print("❌ No entry found to delete.")

# Main loop
while True:
    print("\n🔐 Welcome to SafePass 🔐")
    print("-" * 40)
    print("1. ➕ Add New Credential")
    print("2. 📋 View All")
    print("3. 🔍 Search by Website")
    print("4. 🗑️ Delete an Entry")
    print("5. ❌ Exit")
    print("-" * 40)

    choice = input("👉 Enter your choice: ")

    if choice == "1":
        add_credential()
    elif choice == "2":
        view_credentials()
    elif choice == "3":
        search_credential()
    elif choice == "4":
        delete_credential()
    elif choice == "5":
        print("👋 Exiting... Stay safe!")
        break
    else:
        print("⚠️ Invalid choice. Try again.")
