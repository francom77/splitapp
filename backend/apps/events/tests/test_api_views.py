from datetime import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.core.tests.mixins import ModelViewSetTestCaseMixin
from apps.events.models import Event, Membership
from apps.events.tests.factory import EventsFakeFactory
from apps.profiles.tests.factory import ProfilesFakeFactory


class EventViewSetTestCase(ModelViewSetTestCaseMixin, APITestCase):
    ModelClass = Event
    basename = 'events'
    namespace = 'events'
    creation_method = EventsFakeFactory.make_event

    def setUp(self):
        super(EventViewSetTestCase, self).setUp()
        self.user_profile = ProfilesFakeFactory.make_user_profile(user=self.user)
        self.ModelClass.objects.update(owner=self.user_profile)

    def _get_create_data(self):
        data = {
            'date_time': datetime.now(),
            'name': 'Test Event Creation',
            'max_memberships': 10,
            'suscription_amount': 100,
            'owner': self.user_profile.pk,
        }
        return data

    def _get_update_data(self):
        data = {
            'name': 'Test Event Creation Change',
        }
        return data


class MembershipViewSetTestCase(ModelViewSetTestCaseMixin, APITestCase):
    ModelClass = Membership
    basename = 'memberships'
    namespace = 'events'
    creation_method = EventsFakeFactory.make_membership

    def setUp(self):
        super(MembershipViewSetTestCase, self).setUp()
        self.user_profile = ProfilesFakeFactory.make_user_profile(user=self.user)
        self.event = EventsFakeFactory.make_event()
        self.ModelClass.objects.update(owner=self.user_profile)

    def _get_create_data(self):
        data = {
            'owner': self.user_profile.pk,
            'event': self.event.pk
        }
        return data

    def test_create_with_max_of_members(self):
        self.event.max_memberships = 1
        self.event.save()
        EventsFakeFactory.make_membership(event=self.event)

        data = self._get_create_data()
        url = reverse(
            '{namespace}:{basename}-list'.format(
                namespace=self.namespace,
                basename=self.basename
            )
        )
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put(self):
        pass

    def test_delete(self):
        pass
