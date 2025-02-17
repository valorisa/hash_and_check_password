# Hash and Check Password

This project implements a Python-based solution for securely hashing and verifying passwords using bcrypt.

## Files

- `advanced_bcrypt.py`: A script for advanced bcrypt-based password hashing, allowing users to securely store their passwords.
- `hash_and_check_password.py`: Main file to hash passwords and check their validity by comparing them to stored hashes.
- `password_hasher.py`: Helper script with functions for password hashing and verification.
- `save_salt_&_hash`: A sample file containing the salt and hashed password stored after processing.

## How Password Hashing Works

This project uses the bcrypt algorithm to securely hash and check passwords. Bcrypt is a widely-used hashing algorithm specifically designed for securely storing passwords. The main feature of bcrypt is that it incorporates a "salt" to protect against rainbow table attacks, and it is computationally expensive to make brute-force attacks more difficult.

### Process

1. **Salt Generation**: A random salt is generated before hashing the password. This salt is unique for each password and is combined with the password before hashing.

2. **Password Hashing**: The bcrypt algorithm combines the salt and the password and applies multiple rounds of cryptographic operations to produce a hash. This makes the hashing process slow and resistant to brute-force attacks.

3. **Storing Hash and Salt**: The salt and hashed password are saved together in a format that can be later used for comparison when verifying the password.

4. **Password Verification**: When a user logs in, the system retrieves the stored salt and hash, combines it with the entered password, and verifies if the generated hash matches the stored one.

### Example Code for Hashing a Password

```python
from password_hasher import hash_password

password = "my_secure_password"
hashed_password = hash_password(password)

print("Hashed Password:", hashed_password)

Example Code for Verifying a Password

from password_hasher import check_password

stored_hash = "$2b$18$gZJcF9Xx4QFkE7l7BmSfw.GeSDcH8nkGmWtTpLlrULTYtFfS5qw0W"  # Example stored hash
entered_password = "my_secure_password"

is_valid = check_password(entered_password, stored_hash)

if is_valid:
    print("Password is valid!")
else:
    print("Invalid password!")

save_salt_&_hash Format

The save_salt_&_hash file contains the salt and hashed password in the following JSON format:

{
  "salt": "$2b$18$gZJcF9Xx4QFkE7l7BmSfw.",
  "hashed_password": "$2b$18$gZJcF9Xx4QFkE7l7BmSfw.GeSDcH8nkGmWtTpLlrULTYtFfS5qw0W"
}

This file demonstrates a securely hashed password with a salt, where the first part is the salt ($2b$18$gZJcF9Xx4QFkE7l7BmSfw.) and the second part is the hashed password.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
