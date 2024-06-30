from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from lunchapp.models import Restaurant, Menu, Vote


# Create your tests here.


class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        self.client.login(username='testuser', password='testpassword')

        self.restaurant = Restaurant.objects.create(name='Test Restaurant', owner=self.user)

        self.menu = Menu.objects.create(restaurant=self.restaurant, date='2024-06-30', items='Pizza, Salad')

    def test_create_restaurant(self):
        url = reverse('restaurant-list')
        data = {'name': 'New Restaurant', 'owner': self.user.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 2)
        self.assertEqual(Restaurant.objects.get(id=response.data['id']).name, 'New Restaurant')

    def test_upload_menu(self):
        url = reverse('menu-list')
        data = {'restaurant': self.restaurant.id, 'date': '2024-07-01', 'items': 'Burger, Fries'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(Menu.objects.get(id=response.data['id']).items, 'Burger, Fries')

    def test_get_current_day_menu(self):
        url = reverse('menu-current-day')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_vote_for_menu(self):
        url = reverse('vote-list')
        data = {'menu': self.menu.id, 'date': '2024-06-30'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(Vote.objects.get(id=response.data['id']).menu, self.menu)

    def test_get_voting_results(self):
        Vote.objects.create(user=self.user, menu=self.menu, date='2024-06-30')
        url = reverse('vote-results')
        response = self.client.get(url)
        key = list(response.data.keys())[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[key], 1)

    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.get(reverse('restaurant-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
