from flask import jsonify
from .custom_exceptions import ApiError


def register_error_handlers(app):

    @app.errorhandler(ApiError)
    def handle_api_error(err: ApiError):
        """ Maneja todos los errores personalizados """
        response = jsonify(err.to_dict())
        response.status_code = err.status_code
        return response

    @app.errorhandler(Exception)
    def handle_generic_exception(err: Exception):
        """ Manejo global de errores inesperados """
        print("❌ ERROR NO CONTROLADO:", err)

        response_body = {
            "code": "INTERNAL_SERVER_ERROR",
            "message": str(err),
            "status": "error",
            "data": None
        }

        return jsonify(response_body), 500
