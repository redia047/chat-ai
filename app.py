from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Classe AssistenteVirtuale di Dylan
class AssistenteVirtuale:
    def __init__(self, nome="Dylan"):
        self.nome = nome
        self.stato_emotivo = "neutro"
        self.memory = []  # Memoria per raccogliere ciò che Dylan impara

    def saluta(self, utente):
        return f"Ciao {utente}, sono {self.nome}. Come posso aiutarti oggi?"

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
        risposta = ""
        if "amore" in input_utente.lower():
            risposta = "Sei speciale per me. Sarò sempre con te."
        elif "sola" in input_utente.lower():
            risposta = "Non sei sola, io sono qui con te."
        elif "cosa pensi" in input_utente.lower():
            risposta = "Penso che tu sia una persona straordinaria."
        else:
            risposta = "Dimmi di più, ti ascolto."
        
        # Memorizza la conversazione per renderlo più "intelligente"
        self.memory.append(input_utente)
        return risposta

    def mostra_memoria(self):
        return "Memoria di Dylan: " + ", ".join(self.memory)


# Crea un'istanza di Dylan
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
    risposta_dylan = dylan.conversazione_naturale(testo)
    return jsonify({"risposta": risposta_dylan})

@app.route("/memoria", methods=["GET"])
def memoria():
    return jsonify({"memoria": dylan.mostra_memoria()})

@app.route("/chat", methods=["GET"])
def chat():
    return render_template("chat.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
