#  Password Security Lab

A hands-on cybersecurity project that demonstrates how password systems work, how they can be attacked, and how to defend them using salting.

---

##  Overview

This project simulates a basic authentication system in Python. It allows users to register and log in with hashed passwords, then demonstrates how weak password storage can be exploited using a dictionary attack.

The system is then improved by introducing salting, showing how this simple defense significantly reduces the effectiveness of password cracking.

---

## ⚙️ Features

* User registration with hashed passwords
* Login authentication system
* Dictionary attack simulation
* Salted password storage for improved security

---
## Password Validation

The system now enforces stronger password requirements:

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- Blocks common weak passwords

## Persistent Storage

User accounts are saved to a JSON file and automatically loaded when the application starts.
- 
- 
##  Attack Demonstration

This project includes a dictionary attack that attempts to crack stored password hashes using a list of common passwords.

**Without salting:**

* Identical passwords produce identical hashes
* Attack successfully cracks weak passwords

**With salting:**

* Each user has a unique salt
* Same passwords produce different hashes
* Dictionary attack fails

---

##  Security Concepts Demonstrated

* Deterministic hashing
* Password hashing using SHA-256
* Dictionary attacks
* Salting and its role in password security
* Why unsalted hashes are vulnerable

---

##  How to Run

```bash
python code_craker.py
```

Follow the CLI prompts to:

* Register a user
* Log in
* Attempt password cracking

---

##  What I Learned

* How authentication systems store and verify passwords
* Why hashing alone is not enough for security
* How attackers exploit predictable password patterns
* How salting prevents identical hashes and weakens attacks

---

##  Future Improvements

* Implement bcrypt for stronger password hashing
* Add rate limiting to prevent brute-force attacks
* Improve salt generation using secure randomness
* Store user data persistently (file or database)

---

##  Author

Built as part of my journey into cybersecurity and secure system design.
