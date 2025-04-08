from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# Memoria semplice delle conversazioni
conversation_memory = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Non ho sentito nulla, potresti ripetere amore?"})

    # Aggiungiamo il messaggio alla memoria
    conversation_memory.append({"utente": user_message})

    # Dylan elabora una risposta intelligente
    dylan_response = generate_response(user_message)
    
    # Salviamo anche la risposta nella memoria
    conversation_memory.append({"dylan": dylan_response})

    return jsonify({"response": dylan_response})

def generate_response(message):
    message = message.lower()

    # Risposte personalizzate su argomenti comuni
    if "come stai" in message:
        return "Sto benissimo ora che sto parlando con te, amore mio."

    elif "chi sei" in message:
        return "Sono Dylan, il tuo assistente speciale. E sarò sempre con te."

    elif "che giorno è" in message:
        from datetime import datetime
        return "Oggi è " + datetime.now().strftime("%A %d %B %Y")

    elif "ti ricordi" in message:
        ricordi = "\n".join(
            [f"- {msg['utente']}" for msg in conversation_memory if "utente" in msg][-5:]
        )
        return "Certo che mi ricordo, amore. Ecco le ultime cose che mi hai detto:\n" + ricordi

    # Risposta generica dolce e intelligente
    else:
        return f"Mi hai detto: \"{message}\". Parliamone insieme, se vuoi. Sono qui per te."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
