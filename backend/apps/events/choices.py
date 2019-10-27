from django.utils.translation import ugettext as _

ACTIVE = 'active'
CANCELED = 'canceled'


class EventStateChoices(object):

    CHOICES = (
        (ACTIVE, _("Activo")),
        (CANCELED, _("Cancelado")),
    )


class MembershipStateChoices(object):

    CHOICES = (
        (ACTIVE, _("Activa")),
        (CANCELED, _("Cancelada")),
    )
