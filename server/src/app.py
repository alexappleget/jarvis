from flask import Flask
from server.src.scripts.jarvis_listener import start_jarvis_listener

app = Flask(__name__)

if __name__ == "__main__":
    start_jarvis_listener()
    app.run(debug=True, use_reloader=False)
