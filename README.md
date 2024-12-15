Yuvy: A Local Password Manager

OVERVIEW<br/>
Yuvy is a secure and user-friendly password manager designed to help users store, retrieve, and manage their passwords with ease. Developed with Python, Flask, and the Cryptography library, Yuvy ensures robust encryption of sensitive data while providing a clean and intuitive web interface. This project is ideal for personal use or as a foundation for more advanced password management systems. <br/>

FEATURES<br/>
1.) Secure Password Storage:
Store website credentials (website name, username, and password) with robust encryption using Fernet from the Cryptography library.

2.) Password Retrieval:<br/>
Retrieve stored credentials by entering the corresponding website name.
Decrypted passwords are displayed only after authentication.

3.) Encryption and Key Management:<br/>
Yuvy generates a unique encryption key (key.key) to ensure data security.
Passwords are stored in an encrypted format in a CSV file.

4.) Interactive Web Interface:<br/>
Designed with HTML, CSS, and JavaScript for a seamless user experience.
Features include form validation, fetch API requests, and dynamic content rendering.

5.) Error Handling:<br/>
Displays user-friendly error messages for invalid input or missing data.

TECH STACK<br/>

FRONTEND:<br/>
HTML5: For structuring the web interface.<br/>
CSS3: Custom dark-themed styling.<br/>
JavaScript: Handles form interactions and API requests.<br/>

BACKEND:<br/>
Flask: Lightweight Python framework for API endpoints and routing.<br/>
Cryptography: Encrypts and decrypts password data securely.<br/>
CSV: Acts as a lightweight database for storing credentials.<br/>

SECURITY:<br/>
Employs industry-standard encryption techniques to secure sensitive information.<br/>

HOW YUVY WORKS<br/>
Add Passwords:<br/>
Users can save credentials for various websites by entering the website name, username, and password.
Passwords are encrypted before storage.<br/>

Retrieve Passwords:<br/>
Users can search for stored credentials using the website name.<br/>
Decrypted credentials are displayed in a secure manner.<br/>

Encryption:<br/>
An encryption key is generated upon setup and saved to key.key.
This key is required for encrypting and decrypting passwords.

DEPENDENCIES<br/>
To run Yuvy, the following Python packages are required:<br/>

Flask<br/>
Cryptography<br/>
Install them using the command:

bash<br/>
```pip install -r requirements.txt```

GETTING STARTED<br/>

1. Clone the Repository:<br/>
bash<br/>
```git clone https://github.com/codewyuu/yuvy```
```cd yuvy```

3. Install Dependencies:<br/>
bash<br/>
```pip install -r requirements.txt```

4. Run the Application:<br/>
bash<br/>
```python password.py```

FUTURE ENHANCEMENTS<br/>
-Add user authentication for multi-user support.<br/>
-More functionality to the web interface.<br/>
-future web hosting and deployment.<br/>
-Implement a database (e.g., SQLite or PostgreSQL) for better scalability.<br/>
-Add password strength checks and suggestions.<br/>
-Integrate a mobile-friendly design.<br/>

<br/>
License
© All rights reserved, Yuvraj Sharma, 2024.
