class ApiError(Exception):
    code = "API_ERROR"
    message = "Error en la operación"
    status_code = 400

    def __init__(self, message=None):
        if message:
            self.message = message
        super().__init__(self.message)


    def to_dict(self):
        return {
            "code": self.code,
            "message": self.message,
            "status": "error",
            "data": None
        }


class NotFoundError(ApiError):
    code = "NOT_FOUND"
    message = "Recurso no encontrado"
    status_code = 404


class UnauthorizedError(ApiError):
    code = "UNAUTHORIZED"
    message = "No autorizado"
    status_code = 401


class ForbiddenError(ApiError):
    code = "FORBIDDEN"
    message = "Acceso prohibido"
    status_code = 403


class BadRequestError(ApiError):
    code = "BAD_REQUEST"
    message = "Solicitud inválida"
    status_code = 400


class ConflictError(ApiError):
    code = "CONFLICT"
    message = "Conflicto en la operación"
    status_code = 409


class ValidationError(ApiError):
    code = "VALIDATION_ERROR"
    message = "Error de validación"
    status_code = 422


class BusinessLogicError(ApiError):
    code = "BUSINESS_LOGIC_ERROR"
    message = "Reglas de negocio no cumplidas"
    status_code = 422


class DatabaseError(ApiError):
    code = "DATABASE_ERROR"
    message = "Error en base de datos"
    status_code = 500
