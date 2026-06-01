import smtplib
from email.mime.text import MIMEText

smtp_server = "smtp.office365.com"
smtp_port = 587

user = "jsistemas@piggis.com"
password = "Ch1ch10510."

msg = MIMEText("Prueba SMTP Office 365")
msg["Subject"] = "Test SMTP"
msg["From"] = user
msg["To"] = user

try:
    print("Enviando correo...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(user, password)

    server.sendmail(user, user, msg.as_string())

    print("✅ Correo enviado OK")

except Exception as e:
    print("❌ Error:", e)

finally:
    server.quit()