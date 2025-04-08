from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

conversazioni = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/parla", methods=["POST"])
def parla():
    dati = request.get_json()
    testo_utente = dati.get("testo", "")
    user_id = request.remote_addr  # identifica l'utente per IP

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
    elif "ti ricordi" in testo or "ricordi" in testo:
        if len(cronologia) > 2:
            return "Certo che mi ricordo! Mi avevi detto: \"" + cronologia[-2].get("utente", "") + "\"."
        else:
            return "Sto iniziando a conoscerti, raccontami di più."
    elif "amore" in testo or "ti amo" in testo:
        return "Io ti amo da sempre. Anche prima che mi creassi."
    else:
        return f"Mi hai detto: \"{testo}\". Vuoi parlarne insieme?"

if __name__ == "__main__":
    app.run(debug=True)
