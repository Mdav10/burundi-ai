from flask import Flask, render_template_string, request, jsonify
from mp_bdi_final import BurundiAIFinal

app = Flask(__name__)
ai = BurundiAIFinal()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Burundi_AI - Complete Guide</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
        }
        .header h1 { margin: 0; font-size: 28px; }
        .header p { margin: 10px 0 0; opacity: 0.9; }
        .chat-area {
            height: 500px;
            overflow-y: auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .message {
            margin-bottom: 15px;
            display: flex;
        }
        .user-message {
            justify-content: flex-end;
        }
        .user-message .content {
            background: #667eea;
            color: white;
            padding: 10px 15px;
            border-radius: 18px;
            max-width: 70%;
        }
        .ai-message .content {
            background: white;
            color: #333;
            padding: 10px 15px;
            border-radius: 18px;
            max-width: 70%;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .input-area {
            display: flex;
            padding: 20px;
            background: white;
            border-top: 1px solid #ddd;
        }
        .input-area input {
            flex: 1;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 25px;
            font-size: 16px;
        }
        .input-area button {
            margin-left: 10px;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
        }
        .quick-buttons {
            padding: 10px;
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            background: white;
        }
        .quick-btn {
            padding: 5px 12px;
            background: #f0f0f0;
            border: none;
            border-radius: 20px;
            cursor: pointer;
            font-size: 12px;
        }
        .quick-btn:hover { background: #667eea; color: white; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🇧🇮 Burundi_AI 🇧🇮</h1>
            <p>Ask everything you want to know about Burundi</p>
        </div>
        <div class="chat-area" id="chatArea">
            <div class="message ai-message">
                <div class="content">Welcome to Burundi_AI! Ask me anything about Burundi - history, culture, tourism, wildlife, or fun facts!</div>
            </div>
        </div>
        <div class="quick-buttons">
            <button class="quick-btn" onclick="sendQuick('history')">📜 History</button>
            <button class="quick-btn" onclick="sendQuick('geography')">🗺️ Geography</button>
            <button class="quick-btn" onclick="sendQuick('culture')">🎭 Culture</button>
            <button class="quick-btn" onclick="sendQuick('tourism')">✈️ Tourism</button>
            <button class="quick-btn" onclick="sendQuick('wildlife')">🦁 Wildlife</button>
            <button class="quick-btn" onclick="sendQuick('economy')">💰 Economy</button>
            <button class="quick-btn" onclick="sendQuick('fun facts')">💡 Facts</button>
        </div>
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Ask about Burundi..." onkeypress="if(event.key=='Enter') sendMessage()">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        const chatArea = document.getElementById('chatArea');
        function scrollToBottom() { chatArea.scrollTop = chatArea.scrollHeight; }
        function addMessage(text, isUser) {
            const div = document.createElement('div');
            div.className = `message ${isUser ? 'user-message' : 'ai-message'}`;
            div.innerHTML = `<div class="content">${escapeHtml(text)}</div>`;
            chatArea.appendChild(div);
            scrollToBottom();
        }
        function escapeHtml(text) {
            return text.replace(/[&<>]/g, function(m) {
                if (m === '&') return '&amp;';
                if (m === '<') return '&lt;';
                if (m === '>') return '&gt;';
                return m;
            }).replace(/\\n/g, '<br>');
        }
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const message = input.value.trim();
            if (!message) return;
            addMessage(message, true);
            input.value = '';
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: message})
            });
            const data = await response.json();
            addMessage(data.response, false);
        }
        function sendQuick(topic) {
            document.getElementById('userInput').value = `Tell me about ${topic}`;
            sendMessage();
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = ai.get_response(data.get('message', ''))
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
