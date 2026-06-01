# app/email/service.py

from app.email.repository import EmailRepository
from app.core.email_service import EmailService
from app.models.email_model import Email


import traceback

class EmailWorkerService:

    @staticmethod
    def procesar_emails():

        pendientes = EmailRepository.get_pending_emails()
        email_service = EmailService()

        enviados = 0
        errores = 0

        for item in pendientes:

            try:
                EmailRepository.mark_as_processing(item.id_mensaje)

                email = Email(
                    to=str(item.destino_correo or ""),
                    subject=str(item.asunto_correo or ""),
                    body=str(item.mensaje_correo or "")
                )

                email_service.send(email)

                EmailRepository.mark_as_sent(item.id_mensaje)

                print(f"✅ Enviado ID {item.id_mensaje}")

                enviados += 1

            except Exception as e:

                errores += 1

                print(f"❌ Error ID {item.id_mensaje}: {e}")
                print(traceback.format_exc())

                EmailRepository.mark_as_error(
                    item.id_mensaje,
                    error=str(e)
                )

        return {
            "pendientes": len(pendientes),
            "enviados": enviados,
            "errores": errores
        }