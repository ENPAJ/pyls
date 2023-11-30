import os

repertoire = input("Entrez le chemin du répertoire : ")

# Valider ou échapper l'entrée utilisateur pour éviter les injections de commandes
# Utilisez toujours des méthodes plus sécurisées selon le contexte d'utilisation réel.
repertoire = os.path.abspath(os.path.expanduser(repertoire))

# Vérifiez le système d'exploitation pour choisir la commande appropriée
if os.name == 'posix':
    os.system(f"ls {repertoire}")
elif os.name == 'nt':
    os.system(f"dir {repertoire}")
else:
    print("Système d'exploitation non pris en charge.")
