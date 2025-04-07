<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat con Dylan</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .chat-box {
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .chat-messages {
            max-height: 400px;
            overflow-y: auto;
            margin-bottom: 20px;
        }
        .chat-input {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        .send-btn {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        .send-btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Benvenuto nella chat con Dylan!</h1>
    <div class="chat-box">
        <div class="chat-messages" id="chat-messages">
            <!-- I messaggi verranno visualizzati qui -->
        </div>
        <input type="text" id="user-input" class="chat-input" placeholder="Scrivi un messaggio..." />
        <button class="send-btn" onclick="sendMessage()">Invia</button>
    </div>

    <script>
        function sendMessage() {
            const userMessage = document.getElementById("user-input").value;
            if (userMessage.trim() === "") return;

            // Aggiungi il messaggio dell'utente alla chat
            const chatMessages = document.getElementById("chat-messages");
            const userMessageElement = document.createElement("div");
            userMessageElement.textContent = "Tu: " + userMessage;
            chatMessages.appendChild(userMessageElement);

            // Pulisci l'input
            document.getElementById("user-input").value = "";

            // Simula una risposta dall'assistente (puoi sostituirlo con una chiamata API per un assistente reale)
            const botMessageElement = document.createElement("div");
            botMessageElement.textContent = "Dylan: " + "Sto pensando alla tua risposta...";
            chatMessages.appendChild(botMessageElement);

            // Scorri verso il basso per vedere l'ultimo messaggio
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    </script>
</body>
</html>
