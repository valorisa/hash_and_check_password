import bcrypt

# Mot de passe à hacher
password = b"mypassword"

# Générer un sel et hacher le mot de passe
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Afficher le mot de passe haché
print("Mot de passe haché:", hashed)

# Vérifier un mot de passe
password_to_check = b"mypassword"
is_correct = bcrypt.checkpw(password_to_check, hashed)

# Afficher le résultat de la vérification
print("Le mot de passe est-il correct ?", is_correct)

