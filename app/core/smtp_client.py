import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config.settings import SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD


class SMTPClient:

    def __init__(self):
        self.server = SMTP_SERVER
        self.port = SMTP_PORT
        self.user = EMAIL_USER
        self.password = EMAIL_PASSWORD

    def send_email(self, email):

        print(f"Preparando correo para: {email.to}")
        print(f"Asunto: {email.subject}")
        print(f"Cuerpo: {email.body}")
        print(f"Servidor: {self.server}")
        print(f"Puerto: {self.port}")
        print(f"Usuario: {self.user}")
        print(f"Contraseña: {self.password}")   
        print("Enviando correo...")

        recipients = [x.strip() for x in email.to.split(",") if x.strip()]

        msg = MIMEMultipart()
        msg["From"] = self.user
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = email.subject

        msg.attach(MIMEText(email.body, "html"))

        try:
            server = smtplib.SMTP(self.server, self.port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.user, self.password)

            server.sendmail(self.user, recipients, msg.as_string())

            print("✅ Correo enviado correctamente")

        except Exception as e:
            print("❌ Error:", e)

        finally:
            server.quit()