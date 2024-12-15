import csv
import os
from cryptography.fernet import Fernet

passwords = []

# Save the key to a file
def save_key():
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the key from a file
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Check if key exists; if not, generate and save it
if os.path.exists("key.key"):
    key = load_key()
else:
    key = Fernet.generate_key()
    save_key()
cipher_suite = Fernet(key)


def encrypt_password(password):
    return cipher_suite.encrypt(password.encode())


def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password).decode()


def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")
    encrypted_password = encrypt_password(password)
    passwords.append({
        "website": website,
        "username": username,
        "password": encrypted_password
    })
    with open('passwords.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, username, encrypted_password.decode()])


def get_password(website):
    if not passwords:
        print("No passwords stored yet!")
        return

    for entry in passwords:
        if entry["website"] == website:
            username = entry["username"]
            encrypted_password = entry["password"]
            decrypted_password = decrypt_password(encrypted_password)
            print(f"Website: {website}")
            print(f"Username: {username}")
            print(f"Password: {decrypted_password}")
            return
    print("Website not found")


if os.path.exists('passwords.csv'):
    with open('passwords.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            passwords.append({
                "website": row[0],
                "username": row[1],
                "password": row[2].encode()  # Convert back to bytes
            })
else:
    with open('passwords.csv', mode='w', newline='') as file:
        pass

while True:
    print("\n1. Add Password")
    print("2. Get Password")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_password()
    elif choice == '2':
        website = input("Enter website: ")
        get_password(website)
    elif choice == '3':
        break
    else:
        print("Invalid choice")
