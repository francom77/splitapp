from decimal import Decimal
from mixer.backend.django import Mixer


class WalletFakeFactory(object):
    '''
    Use to create fake objects from this app
    '''

    default_movement = {
        'amount': Decimal('100'),
    }

    @classmethod
    def make_movement(cls, *args, **kwargs):
        params = cls.default_movement.copy()
        params.update(kwargs)
        instance = Mixer().blend('wallet.Movement', **params)

        return instance
