Yuvy: A Local Password Manager

OVERVIEW
Yuvy is a secure and user-friendly password manager designed to help users store, retrieve, and manage their passwords with ease. Developed with Python, Flask, and the Cryptography library, Yuvy ensures robust encryption of sensitive data while providing a clean and intuitive web interface. This project is ideal for personal use or as a foundation for more advanced password management systems. <br/>

FEATURES
1.) Secure Password Storage:
Store website credentials (website name, username, and password) with robust encryption using Fernet from the Cryptography library.

2.) Password Retrieval:
Retrieve stored credentials by entering the corresponding website name.
Decrypted passwords are displayed only after authentication.

3.) Encryption and Key Management:
Yuvy generates a unique encryption key (key.key) to ensure data security.
Passwords are stored in an encrypted format in a CSV file.

4.) Interactive Web Interface:
Designed with HTML, CSS, and JavaScript for a seamless user experience.
Features include form validation, fetch API requests, and dynamic content rendering.

5.) Error Handling:
Displays user-friendly error messages for invalid input or missing data.

TECH STACK

FRONTEND:
HTML5: For structuring the web interface.
CSS3: Custom dark-themed styling.
JavaScript: Handles form interactions and API requests.

BACKEND:
Flask: Lightweight Python framework for API endpoints and routing.
Cryptography: Encrypts and decrypts password data securely.
CSV: Acts as a lightweight database for storing credentials.

SECURITY:
Employs industry-standard encryption techniques to secure sensitive information.

HOW YUVY WORKS
Add Passwords:
Users can save credentials for various websites by entering the website name, username, and password.
Passwords are encrypted before storage.

Retrieve Passwords:
Users can search for stored credentials using the website name.
Decrypted credentials are displayed in a secure manner.

Encryption:
An encryption key is generated upon setup and saved to key.key.
This key is required for encrypting and decrypting passwords.

DEPENDENCIES
To run Yuvy, the following Python packages are required:

Flask
Cryptography
Install them using the command:

bash
'''pip install -r requirements.txt'''

GETTING STARTED

1. Clone the Repository:
bash
'''git clone https://github.com/codeyuu/yuvy.git
cd yuvy'''

3. Install Dependencies:
bash
'''pip install -r requirements.txt'''

4. Run the Application:
bash
'''python password.py'''

FUTURE ENHANCEMENTS
-Add user authentication for multi-user support.
-More functionality to the web interface.
-future web hosting and deployment.
-Implement a database (e.g., SQLite or PostgreSQL) for better scalability.
-Add password strength checks and suggestions.
-Integrate a mobile-friendly design.


License
© All rights reserved, Yuvraj Sharma, 2024.
