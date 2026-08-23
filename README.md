# 🔐 Password Security Lab

A hands-on cybersecurity project that demonstrates how password authentication systems evolve from insecure password storage to a more secure web-based authentication system using bcrypt.

This project was built progressively to explore not only how passwords are stored and verified, but also why certain approaches are vulnerable and how modern password hashing techniques improve security.

---

## 🧪 Project Evolution

The project contains multiple versions of the authentication system, with each version introducing a security improvement.

### Version 1 — SHA-256 Without Salt

The first version demonstrates basic password hashing using SHA-256.

Passwords are hashed before being stored, but no salt is used.

This demonstrates an important weakness:

- Identical passwords generate identical hashes
- Predictable passwords remain vulnerable to dictionary attacks
- Fast hashing algorithms such as SHA-256 are not ideal for password storage

File:

`v1_no_salt.py`

---

### Version 2 — SHA-256 With Salt

The second version introduces salting.

A unique salt is added to each password before hashing, preventing identical passwords from producing identical hashes.

This demonstrates how salting makes precomputed attacks significantly less effective.

File:

`v2_salted_version.py`

---

### Version 3 — bcrypt Authentication

The third version replaces SHA-256 password storage with bcrypt.

bcrypt automatically handles salt generation and is intentionally computationally expensive, making brute-force password attacks more difficult.

This version also introduces login-attempt tracking and account lockout behavior.

File:

`v3_bcrypt.py`

---

## 🌐 Flask Web Application

The project was later expanded from a command-line program into a Flask web application.

The application provides a browser-based interface where users can:

- Register an account
- Log in with their credentials
- Have passwords validated before registration
- Authenticate using bcrypt password verification
- Track failed login attempts
- Lock accounts after repeated failed login attempts
- Access a protected dashboard after successful authentication
- Log out of the application

The Flask application is located in:

`app.py`

HTML templates are stored in:

`templates/`

CSS styling is stored in:

`static/`

---

## 🔑 Password Validation

New passwords must meet several requirements:

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- Common weak passwords are rejected

These checks demonstrate how applications can enforce stronger password policies before credentials are stored.

---

## 💾 Persistent User Storage

Registered users are stored locally in:

`users.json`

The application loads existing users when it starts and saves changes when account information is updated.

For security and privacy, the real `users.json` file is excluded from Git using `.gitignore`.

An empty example file is included instead:

`users.example.json`

This allows the project structure to be demonstrated without publishing actual account data or password hashes.

---

## 🛡️ Security Concepts Demonstrated

This project explores several important authentication and cybersecurity concepts:

- Password hashing
- SHA-256
- Deterministic hashing
- Dictionary attacks
- Password salting
- bcrypt password hashing
- Password validation
- Authentication
- Login attempt tracking
- Account lockout
- Persistent user storage
- Protecting user data from source control

---

## 📁 Project Structure

```text
password-security-lab/
│
├── app.py
├── v1_no_salt.py
├── v2_salted_version.py
├── v3_bcrypt.py
├── users.example.json
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── register.html
    └── dashboard.html
```

---

## 🚀 Running the Flask Application

### 1. Install the required packages

```bash
pip install flask bcrypt
```

### 2. Start the application

```bash
python app.py
```

### 3. Open the application in your browser

```text
http://127.0.0.1:5000
```

You can then register a test account and use it to log in.

The application will create and use local user data without requiring that data to be committed to the repository.

---

## 🎯 What I Learned

Building this project helped me understand the progression from basic password hashing to more practical authentication security.

Key takeaways include:

- Why storing plaintext passwords is unsafe
- Why hashing alone does not automatically make password storage secure
- How dictionary attacks exploit predictable passwords
- Why salts prevent identical passwords from producing identical hashes
- Why bcrypt is better suited for password storage than general-purpose hashing algorithms
- How authentication state can be integrated into a Flask web application
- How failed login attempts can be tracked to reduce brute-force attempts
- Why sensitive application data should not be committed to source control

---

## 🔮 Future Improvements

Possible future improvements include:

- Replace JSON storage with a database
- Add password reset functionality
- Add email verification
- Improve session security
- Add CSRF protection
- Add automated security tests
- Add configurable rate limiting
- Deploy the application in a production environment

---

## 👨‍💻 Author

Built as a hands-on project exploring cybersecurity, authentication, Python, and secure software development.