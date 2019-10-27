import uuid

from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from apps.core.models import BaseModel
from apps.events.models import EventStateChoices, MembershipStateChoices


class Event(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name="events",
        related_query_name="event",
    )
    date_time = models.DateTimeField()
    name = models.CharField(max_legth=250)
    max_memberships = models.PositiveIntegerField(null=True, blank=True)
    suscription_amount = models.DecimalField(
        validators=(MinValueValidator(0),),
        decimal_places=2,
        max_digits=10,
        default=Decimal('0'),
    )
    state = models.CharField(
        max_length=25,
        choices=EventStateChoices.CHOICES,
        default=EventStateChoices.ACTIVE
    )


class Membership(BaseModel):
    profile = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name="memberships",
        related_query_name="membership",
    )
    event = models.ForeignKey(
        'events.Event',
        on_delete=models.CASCADE,
        related_name="memberships",
        related_query_name="membership",
    )
    state = models.CharField(
        max_length=25,
        choices=MembershipStateChoices.CHOICES,
        default=MembershipStateChoices.ACTIVE
    )
