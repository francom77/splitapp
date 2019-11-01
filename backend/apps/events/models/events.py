import uuid
from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from apps.core.models import BaseModel
from apps.events.choices import EventStateChoices, MembershipStateChoices
from apps.events.state_machines import (
    EventStateMachine,
    MembershipStateMachine,
)


class Event(BaseModel):

    state_machine = EventStateMachine.TRANSITIONS

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        'profiles.UserProfile',
        on_delete=models.CASCADE,
        related_name="events",
        related_query_name="event",
    )
    date_time = models.DateTimeField()
    name = models.CharField(max_length=250)
    max_memberships = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        null=True,
        blank=True,
    )
    suscription_amount = models.DecimalField(
        validators=[MinValueValidator(Decimal('0'))],
        decimal_places=2,
        max_digits=10,
        default=Decimal('0'),
    )
    state = models.CharField(
        max_length=25,
        choices=EventStateChoices.CHOICES,
        default=EventStateChoices.ACTIVE
    )

    def is_full(self):
        paid_memberships = self.memberships.filter(
            state=MembershipStateChoices.PAID
        ).count()
        return (
            self.max_memberships is not None and
            paid_memberships >= self.max_memberships
        )


class Membership(BaseModel):

    unique_together = ['owner', 'event']

    state_machine = MembershipStateMachine.TRANSITIONS

    owner = models.ForeignKey(
        'profiles.UserProfile',
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
        default=MembershipStateChoices.INITIAL
    )
