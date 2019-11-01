class CurrentProfileDefault:
    def set_context(self, serializer_field):
        self.userprofile = serializer_field.context['request'].user.userprofile

    def __call__(self):
        return self.userprofile

    def __repr__(self):
        return '%s()' % self.__class__.__name__
