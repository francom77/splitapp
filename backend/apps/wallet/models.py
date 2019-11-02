from decimal import Decimal

from django.db import models

from apps.core.models import BaseModel


class Movement(BaseModel):
    owner = models.ForeignKey(
        'profiles.UserProfile',
        on_delete=models.CASCADE,
        related_name="movements",
        related_query_name="movement",
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=Decimal('0'),
    )
    description = models.TextField()


class MercadoPagoPayment(Movement):
    pass


class MembershipPayment(Movement):
    membership = models.ForeignKey(
        'events.Membership',
        on_delete=models.CASCADE,
        related_name="payments",
        related_query_name="payment",
    )


class PaymentReceived(Movement):
    sender = models.ForeignKey(
        'profiles.UserProfile',
        on_delete=models.CASCADE,
        related_name="sent_payment",
        related_query_name="sent_payments",
    )


class Withdrawal(Movement):
    pass
