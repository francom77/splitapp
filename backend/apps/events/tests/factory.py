from datetime import datetime
from decimal import Decimal
from dateutil.relativedelta import relativedelta
from mixer.backend.django import Mixer


class EventsFakeFactory(object):
    '''
    Use to create fake objects from this app
    '''

    default_event = {
        'date_time': datetime.today() + relativedelta(days=150),
        'name': 'Test event',
        'suscription_amount': Decimal('100')
    }

    @classmethod
    def make_event(cls, *args, **kwargs):
        params = cls.default_event.copy()
        params.update(kwargs)
        instance = Mixer().blend('events.Event', **params)

        return instance
