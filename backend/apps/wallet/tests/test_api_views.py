from rest_framework.test import APITestCase

from apps.core.tests.mixins import ModelViewSetTestCaseMixin
from apps.profiles.tests.factory import ProfilesFakeFactory
from apps.wallet.models import Movement
from apps.wallet.tests.factory import WalletFakeFactory


class MovementViewSetTestCase(ModelViewSetTestCaseMixin, APITestCase):
    ModelClass = Movement
    basename = 'movements'
    namespace = 'wallet'
    creation_method = WalletFakeFactory.make_movement

    def setUp(self):
        super(MovementViewSetTestCase, self).setUp()
        self.user_profile = ProfilesFakeFactory.make_user_profile(user=self.user)
        self.ModelClass.objects.update(owner=self.user_profile)

    def test_post(self):
        pass

    def test_put(self):
        pass

    def test_delete(self):
        pass
