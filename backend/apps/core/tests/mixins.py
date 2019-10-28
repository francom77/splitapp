from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status


class ModelViewSetTestCaseMixin(object):

    basename = None
    namespace = None
    ModelClass = None
    initial_count = 3
    creation_method = None

    def _get_create_data(self):
        pass

    def _get_update_data(self):
        pass

    def setUp(self):
        self.user = User.objects.create(username='test', is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

        for x in range(0, self.initial_count):
            self.creation_method()

    def test_post(self):
        data = self._get_create_data()
        url = reverse(
            '{namespace}:{basename}-list'.format(
                namespace=self.namespace,
                basename=self.basename
            )
        )
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.ModelClass.objects.count(), self.initial_count + 1)

    def test_put(self):
        data = self._get_update_data()
        self.url = reverse(
            '{namespace}:{basename}-detail'.format(
                namespace=self.namespace,
                basename=self.basename
            ),
            kwargs={'pk': self.ModelClass.objects.earliest('pk').pk}
        )
        response = self.client.patch(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_list(self):
        url = reverse(
            '{namespace}:{basename}-list'.format(
                namespace=self.namespace,
                basename=self.basename
            )
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), self.initial_count)

    def test_get_detail(self):
        self.url = reverse(
            '{namespace}:{basename}-detail'.format(
                namespace=self.namespace,
                basename=self.basename
            ),
            kwargs={'pk': self.ModelClass.objects.earliest('pk').pk}
        )
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        self.url = reverse(
            '{namespace}:{basename}-detail'.format(
                namespace=self.namespace,
                basename=self.basename
            ),
            kwargs={'pk': self.ModelClass.objects.earliest('pk').pk}
        )
        response = self.client.delete(self.url, format='json')
        self.assertEqual(self.ModelClass.objects.count(), self.initial_count - 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
