from flask import Blueprint, request, jsonify
from app.models.email_model import Email
from app.core.email_service import EmailService

email_bp = Blueprint("email_bp", __name__)


@email_bp.route("/", methods=["POST"])
def send_email():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Body requerido"}), 400

    if not data.get("to") or not data.get("subject") or not data.get("body"):
        return jsonify({"error": "Faltan campos"}), 400

    email = Email(
        to=data["to"],
        subject=data["subject"],
        body=data["body"]
    )

    service = EmailService()
    service.send(email)

    return jsonify({
        "message": "Correo enviado correctamente"
    }), 200