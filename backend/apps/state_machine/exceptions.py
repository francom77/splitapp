# -*- coding: utf-8 -*-


class StopStateChange(Exception):
    """Raise when you want stop state change, in the before callback"""


class WrongState(Exception):
    pass
