from django.utils.translation import ugettext as _

from apps.events import constants as cts


class EventStateChoices(object):

    CHOICES = (
        (cts.ACTIVE, _("Activo")),
        (cts.CANCELED, _("Cancelado")),
    )


class MembershipStateChoices(object):

    CHOICES = (
        (cts.ACTIVE, _("Activa")),
        (cts.PAID, _("Pagada")),
        (cts.CANCELED, _("Cancelada")),
    )
