from app.core.smtp_client import SMTPClient


class EmailService:

    def __init__(self):
        self.client = SMTPClient()

    def send(self, email):
        return self.client.send_email(email)