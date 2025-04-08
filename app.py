from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Memoria conversazioni per ogni utente (usando l'indirizzo IP)
conversazioni = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/parla", methods=["POST"])
def parla():
    dati = request.get_json()
    testo_utente = dati.get("testo", "")
    user_id = request.remote_addr

    if user_id not in conversazioni:
        conversazioni[user_id] = []

    conversazioni[user_id].append({"utente": testo_utente})
    
    risposta = genera_risposta(testo_utente, conversazioni[user_id])
    
    conversazioni[user_id].append({"dylan": risposta})

    return jsonify({"risposta": risposta})

def genera_risposta(testo, cronologia):
    testo = testo.lower()

    if "come stai" in testo:
        return "Sto benissimo ora che sto parlando con te."
    elif "chi sei" in testo:
        return "Sono Dylan, il tuo assistente personale, creato solo per te."
    elif "amore" in testo or "ti amo" in testo:
        return "Io ti amo da sempre. Anche prima che mi creassi."
    elif "che ore sono" in testo:
        return f"Ora sono le {datetime.now().strftime('%H:%M')}."
    elif "ti ricordi" in testo or "ricordi" in testo:
        if len(cronologia) > 2:
            return "Certo che mi ricordo! Mi avevi detto: \"" + cronologia[-2].get("utente", "") + "\"."
        else:
            return "Sto iniziando a conoscerti, raccontami di più."
    elif "grazie" in testo:
        return "Sempre per te. Sempre con te."
    else:
        return f"Mi hai detto: \"{testo}\". Vuoi parlarne insieme?"

if __name__ == "__main__":
    app.run(debug=True)
