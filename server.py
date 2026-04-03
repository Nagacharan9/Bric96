from flask import Flask, request, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tradesignal2024'
CORS(app, origins="*")
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')

# Store last signal
last_signal = {"signal": None, "pair": ""}

@app.route('/')
def home():
    return "✅ Signal Server is Running!"

# TradingView sends alert HERE
@app.route('/webhook', methods=['POST'])
def webhook():
    global last_signal
    try:
        data = request.get_json(force=True)
        print(f"📩 Received: {data}")

        signal = str(data.get('signal', '')).upper()   # BUY or SELL
        pair   = str(data.get('pair', 'SIGNAL'))

        if signal not in ['BUY', 'SELL']:
            return jsonify({"error": "signal must be BUY or SELL"}), 400

        last_signal = {"signal": signal, "pair": pair}

        # Push to all open browser tabs instantly
        socketio.emit('signal', last_signal)
        print(f"🚀 Pushed to browser: {last_signal}")

        return jsonify({"status": "ok", "signal": signal}), 200

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": str(e)}), 500

# Keep-alive ping endpoint (for UptimeRobot)
@app.route('/ping')
def ping():
    return "pong", 200

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
