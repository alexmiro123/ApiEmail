from app.database.connection import fetchall, execute
from app.models.mensajeria_model import Mensajeria


class EmailRepository:

    GET_PENDING_SQL = """
        SELECT
            ID_MENSAJE,
            DESTINO_SMS,
            DESTINO_CORREO,
            MENSAJE_SMS,
            ESTADO_SMS,
            ESTADO_CORREO,
            CREA_USR,
            CREA_FECHA,
            MOD_USR,
            MOD_FECHA,
            MAC_ADDRESS,
            MODULO,
            ENVIA_SMS,
            ENVIA_CORREO,
            MENSAJE_CORREO_RES,
            ASUNTO_CORREO,
            QUIEN_ENVIA_CORREO,
            RESPONDER_CORREO_A,
            TIPO,
            ADJUNTOS,
            PROCESO_ENVIO,
            DBMS_LOB.SUBSTR(MENSAJE_CORREO, 4000, 1) AS MENSAJE_CORREO
        FROM DATA_USR.GEN_MENSAJERIA
        WHERE ESTADO_CORREO = 0
          AND ENVIA_CORREO = 1
    """

    @staticmethod
    def get_pending_emails():

        rows = fetchall(EmailRepository.GET_PENDING_SQL, {})

        if not rows:
            return []

        return [Mensajeria(row) for row in rows]
    


    # =========================
    # EN PROCESO
    # =========================
    @staticmethod
    def mark_as_processing(id_mensaje):
        sql = """
            UPDATE DATA_USR.GEN_MENSAJERIA
            SET ESTADO_CORREO = 1,
                MOD_FECHA = SYSDATE
            WHERE ID_MENSAJE = :id
        """
        execute(sql, {"id": id_mensaje})

    # =========================
    # ENVIADO OK
    # =========================
    @staticmethod
    def mark_as_sent(id_mensaje):
        sql = """
            UPDATE DATA_USR.GEN_MENSAJERIA
            SET ESTADO_CORREO = 2,
                MOD_FECHA = SYSDATE
            WHERE ID_MENSAJE = :id
        """
        execute(sql, {"id": id_mensaje})

    # =========================
    # ERROR (TE FALTABA ESTO)
    # =========================
    @staticmethod
    def mark_as_error(id_mensaje, error=None):
        sql = """
            UPDATE DATA_USR.GEN_MENSAJERIA
            SET ESTADO_CORREO = 3,
                MENSAJE_CORREO_RES = :error,
                MOD_FECHA = SYSDATE
            WHERE ID_MENSAJE = :id
        """
        execute(sql, {
            "id": id_mensaje,
            "error": str(error)
        })