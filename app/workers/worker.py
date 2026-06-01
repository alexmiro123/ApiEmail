# app/workers/email_worker.py

import time
from app.email.service import EmailWorkerService


def email_worker():

    while True:

        print("🔄 Revisando correos pendientes...")

        result = EmailWorkerService.procesar_emails()

        print(f"📊 Resultado: {result}")

        time.sleep(30)