from mixer.backend.django import Mixer


class ProfilesFakeFactory(object):
    '''
    Use to create fake objects from this app
    '''

    default_event = {
    }

    @classmethod
    def make_user_profile(cls, *args, **kwargs):
        params = cls.default_event.copy()
        params.update(kwargs)
        instance = Mixer().blend('profiles.UserProfile', **params)

        return instance
