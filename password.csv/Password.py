from flask import Flask, render_template, request, jsonify
import csv
from cryptography.fernet import Fernet

app = Flask(__name__)

# Load key from file or generate it
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

key = load_key()  # Load from file
cipher_suite = Fernet(key)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-password', methods=['POST'])
def add_password():
    # Receiving data from JavaScript using JSON
    data = request.get_json()
    website = data['website']
    username = data['username']
    password = data['password']

    encrypted_password = cipher_suite.encrypt(password.encode())

    # Save to CSV or database
    with open('passwords.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, username, encrypted_password.decode()])

    return jsonify({"message": "Password added successfully!"})

@app.route('/get-password', methods=['GET'])
def get_password():
    website = request.args.get('website')
    
    # Search for the website in your password file and decrypt
    with open('passwords.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == website:
                username = row[1]
                decrypted_password = cipher_suite.decrypt(row[2].encode()).decode()
                return jsonify({"website": website, "username": username, "password": decrypted_password})

    return jsonify({"message": "Website not found!"})

if __name__ == "__main__":
    app.run(debug=True)
