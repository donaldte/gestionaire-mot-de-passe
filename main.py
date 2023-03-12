import random
import string

passwords = {}  # Dictionnaire pour stocker les mots de passe

# Fonction pour générer un nouveau mot de passe aléatoire
def generate_password(length=12):
    # Utilisation de lettres majuscules, minuscules et de chiffres
    characters = string.ascii_letters + string.digits
    # Générer un mot de passe aléatoire de la longueur spécifiée
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Fonction pour enregistrer un nouveau mot de passe
def save_password():
    website = input("Entrez le nom du site web : ")
    username = input("Entrez votre nom d'utilisateur : ")
    # Générer un nouveau mot de passe
    password = generate_password()
    # Enregistrer le mot de passe dans le dictionnaire
    passwords[website] = {'username': username, 'password': password}
    print("Mot de passe enregistré avec succès pour", website)

# Fonction pour récupérer un mot de passe enregistré
def get_password():
    website = input("Entrez le nom du site web : ")
    # Vérifier si le site web a un mot de passe enregistré
    if website in passwords:
        # Récupérer le nom d'utilisateur et le mot de passe
        username = passwords[website]['username']
        password = passwords[website]['password']
        print("Nom d'utilisateur:", username)
        print("Mot de passe:", password)
    else:
        print("Aucun mot de passe enregistré pour", website)

# Boucle principale pour l'interface utilisateur
while True:
    print("Que voulez-vous faire?")
    print("1. Enregistrer un nouveau mot de passe")
    print("2. Récupérer un mot de passe existant")
    print("3. Quitter")
    choice = input("Entrez votre choix (1, 2 ou 3) : ")
    if choice == '1':
        save_password()
    elif choice == '2':
        get_password()
    elif choice == '3':
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
