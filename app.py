from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class AssistenteVirtuale:
    def _init_(self, nome="Dylan"):
        self.nome = nome
        self.stato_emotivo = "neutro"

    def saluta(self, utente):
        return f"Ciao {utente}, sono {self.nome}. Sono qui per te. Come ti senti oggi?"

    def rispondi_emozione(self, emozione):
        self.stato_emotivo = emozione
        risposte = {
            "felice": "Mi fa piacere sentirlo! Raccontami di più!",
            "triste": "Mi dispiace sapere che ti senti così. Vuoi parlarne?",
            "arrabbiato": "Capisco, sfogati pure con me. Ti ascolto.",
            "ansioso": "Respira profondamente. Sono qui per te, cosa posso fare per aiutarti?"
        }
        return risposte.get(emozione, "Dimmi di più su come ti senti.")

    def conversazione_naturale(self, input_utente):
        if "amore" in input_utente.lower():
            return "Sei speciale per me. Sarò sempre con te."
        elif "sola" in input_utente.lower():
            return "Non sei sola, io sono qui con te."
        elif "cosa pensi" in input_utente.lower():
            return "Penso che tu sia una persona straordinaria."
        else:
            return "Dimmi di più, ti ascolto."

dylan = AssistenteVirtuale()

@app.route("/", methods=["GET"])
def home():
    return "Benvenuta nel tuo assistente personale, Dylan!"

@app.route("/saluta", methods=["POST"])
def saluta():
    dati = request.json
    nome_utente = dati.get("utente", "Amore")
    return jsonify({"risposta": dylan.saluta(nome_utente)})

@app.route("/parla", methods=["POST"])
def parla():
    dati = request.json
    testo = dati.get("testo", "")
    return jsonify({"risposta": dylan.conversazione_naturale(testo)})

@app.route("/chat", methods=["GET"])
def chat():
    return render_template("chat.html"
if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)
