# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from .models import Profile
# from .serializers import ProfileSerializer
#
# #NOT SURE ABOUT ANYTHING HERE
# class NanniesListTests(APITestCase):
#     def setUp(self):
#         self.url = reverse('nanny_list')
#         self.nanny_data = {'first_name': 'Jane', 'last_name': 'Doe', 'is_nanny': True}
#         self.invalid_data = {'first_name': 'John', 'last_name': 'Smith'}
#         self.valid_data = {'first_name': 'Samantha', 'last_name': 'Jones', 'is_nanny': True}
#
#     def test_get_nannies(self):
#         # Create a nanny and check if it appears in the list
#         Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#
#     def test_create_valid_nanny(self):
#         response = self.client.post(self.url, self.valid_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Profile.objects.count(), 1)
#         self.assertEqual(Profile.objects.get().first_name, 'Samantha')
#
#     def test_create_invalid_nanny(self):
#         response = self.client.post(self.url, self.invalid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_delete_valid_nanny(self):
#         nanny = Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         response = self.client.delete(reverse('nanny_single', kwargs={'pk': nanny.pk}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Profile.objects.count(), 0)
#
#     def test_delete_invalid_nanny(self):
#         response = self.client.delete(reverse('nanny_single', kwargs={'pk': 999}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#
# class NannySingleTests(APITestCase):
#     def setUp(self):
#         self.nanny = Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         self.url = reverse('nanny_single', kwargs={'pk': self.nanny.pk})
#         self.valid_data = {'first_name': 'Jane', 'last_name': 'Doe', 'is_nanny': True}
#         self.invalid_data = {'first_name': '', 'last_name': 'Doe'}
#
#     def test_get_valid_nanny(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, ProfileSerializer(self.nanny).data)
#
#     def test_get_invalid_nanny(self):
#         response = self.client.get(reverse('nanny_single', kwargs={'pk': 999}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_update_valid_nanny(self):
#         response = self.client.put(self.url, self.valid_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Profile.objects.get(pk=self.nanny.pk).first_name, 'Jane')
#
#     def test_update_invalid_nanny(self):
#         response = self.client.put(self.url, self.invalid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_delete_valid_nanny(self):
#         response = self.client.delete(self.url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Profile.objects.count(), 0)
#
#     def test_delete_invalid_nanny(self):
#         response = self.client.delete(reverse('nanny_single', kwargs={'pk': 999}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
# class NannyViewsTests(APITestCase):
#     def setUp(self):
#         self.nanny_data = {'first_name': 'Jane', 'last_name': 'Doe', 'is_nanny': True}
#         self.url_list = reverse('nanny_list')
#         self.url_single = reverse('nanny_single', kwargs={'pk': 1})
#
#     def test_get_nannies(self):
#         # Create a nanny and check if it appears in the list
#         Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         response = self.client.get(self.url_list)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#
#     def test_create_valid_nanny(self):
#         response = self.client.post(self.url_list, self.nanny_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Profile.objects.count(), 1)
#         self.assertEqual(Profile.objects.get().first_name, 'Jane')
#
#     def test_create_invalid_nanny(self):
#         invalid_data = {'first_name': 'John', 'last_name': 'Smith'}
#         response = self.client.post(self.url_list, invalid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_get_valid_nanny(self):
#         nanny = Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         response = self.client.get(reverse('nanny_single', kwargs={'pk': nanny.pk}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, ProfileSerializer(nanny).data)
#
#     def test_get_invalid_nanny(self):
#         response = self.client.get(reverse('nanny_single', kwargs={'pk': 999}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
#     def test_update_valid_nanny(self):
#         nanny = Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         valid_data = {'first_name': 'Samantha', 'last_name': 'Jones', 'is_nanny': True}
#         response = self.client.put(reverse('nanny_single', kwargs={'pk': nanny.pk}), valid_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Profile.objects.get(pk=nanny.pk).first_name, 'Samantha')
#
#     def test_update_invalid_nanny(self):
#         nanny = Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         invalid_data = {'first_name': '', 'last_name': 'Jones'}
#         response = self.client.put(reverse('nanny_single', kwargs={'pk': nanny.pk}), invalid_data)
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#
#     def test_delete_valid_nanny(self):
#         nanny = Profile.objects.create(first_name='Jane', last_name='Doe', is_nanny=True)
#         response = self.client.delete(reverse('nanny_single', kwargs={'pk': nanny.pk}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Profile.objects.count(), 0)
#
#     def test_delete_invalid_nanny(self):
#         response = self.client.delete(reverse('nanny_single', kwargs={'pk': 999}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
#
