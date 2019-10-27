from django.db import models

from apps.core.models import BaseHistory
from apps.events.choices import EventStateChoices, MembershipStateChoices


class EventStateHistory(BaseHistory):
    parent_field_name = 'event'
    states_choices = EventStateChoices.CHOICES
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name='histories'
    )


class MembershipStateHistory(BaseHistory):
    parent_field_name = 'membership'
    states_choices = MembershipStateChoices.CHOICES
    membership = models.ForeignKey(
        'events.Membership',
        on_delete=models.CASCADE,
        related_name='histories'
    )
