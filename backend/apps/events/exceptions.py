from rest_framework.exceptions import APIException


class EventIsFullAPIException(APIException):
    status_code = 400
    default_detail = 'La cantidad de miembros ha sido alcanzada'
    default_code = 'event_is_full'
