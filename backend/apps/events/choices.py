from django.utils.translation import ugettext as _

from apps.events import constants as cts


class EventStateChoices(object):
    ACTIVE = cts.ACTIVE
    CANCELED = cts.CANCELED

    CHOICES = (
        (ACTIVE, _("Activo")),
        (CANCELED, _("Cancelado")),
    )


class MembershipStateChoices(object):
    INITIAL = cts.INITIAL
    PAID = cts.PAID
    CANCELED = cts.CANCELED

    CHOICES = (
        (INITIAL, _("Inicial")),
        (PAID, _("Pagada")),
        (CANCELED, _("Cancelada")),
    )
