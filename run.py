from app.main import create_app
from waitress import serve
import threading
import os

from app.workers.worker import email_worker

app = create_app()

def start_worker():
    email_worker()

if __name__ == "__main__":

    # 🚀 arrancar worker en background
    worker_thread = threading.Thread(target=start_worker, daemon=True)
    worker_thread.start()

    # 🚀 detectar entorno
    debug = os.getenv("FLASK_DEBUG", "0") == "1"

    if debug:
        print("🔧 MODO DEBUG (Flask)")
        app.run(host="0.0.0.0", port=5000, debug=True)
    else:
        print("🚀 MODO PRODUCCIÓN (Waitress)")
        serve(app, host="0.0.0.0", port=5003)