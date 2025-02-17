import bcrypt

def hash_password(password):
    # Générer un sel et hacher le mot de passe
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed

def check_password(password, hashed):
    # Vérifier si le mot de passe correspond au hachage
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Exemple d'utilisation
password = "mypassword"
hashed = hash_password(password)
print("Mot de passe haché:", hashed)

password_to_check = "mypassword"
is_correct = check_password(password_to_check, hashed)
print("Le mot de passe est-il correct ?", is_correct)

