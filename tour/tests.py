from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest

from users.models import User, Guide, Member
from tour.models import Tour, Review
from tour.forms import TourForm

# Create your tests here.

class TourViewTestCase(TestCase):

    def setUp(self):

        # Create User
        User.objects.create(username='user1', password=make_password(
            '1234'), email='user1@example.com')

        userguide1 = User.objects.create(username='user2', password=make_password(
            '1234'), email='user2@example.com', is_guide=True)
        guide = Guide.objects.create(
            user=userguide1, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx')
        userguide2 = User.objects.create(username='user3', password=make_password(
            '1234'), email='user2@example.com', is_guide=True)
        guide = Guide.objects.create(
            user=userguide2, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx')

        usermember = User.objects.create(username='user4', password=make_password(
            '1234'), email='user3@example.com', is_member=True)
        member = Member.objects.create(user=usermember, gender='xxx', age='xxx', address='xxx', allergic='xxx', underlying_disease = 'xxx', religion = 'xxx')

        # Create Tour
        Tour.objects.create(t_name='xxx', guide=userguide1, province='xxx', price=2000, period='xxx', amount=10, information='xxx')

    def test_guide_craete_tour_view(self):
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('tour:create_tour'))
        self.assertEqual(response.status_code, 200)

    def test_member_not_see_craete_tour_view(self):
        c = Client()
        user = User.objects.get(username='user4')
        c.force_login(user)
        response = c.get(reverse('tour:create_tour'))
        self.assertEqual(response.status_code, 302)

    def test_create_tour_form(self):
        form_data = {
            't_title': 'test1',
            'province': 'Bangkok',
            'price': 2000,
            'amount': 10,
            'period': '10 hours',
            'img': 'img.png',
            'information': 'information',
        }

        response = self.client.post(reverse('tour:create_tour'), data=form_data)
        self.assertEqual(response.status_code, 302)

        tours = Tour.objects.all()
        self.assertEqual(tours.count(), 1)

    def test_my_tour_view_success(self):
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('tour:my_tour'))
        self.assertEqual(response.status_code, 200)

    def test_my_tour_view_unsuccess(self):
        c = Client()
        user = User.objects.get(username='user1')
        c.force_login(user)
        response = c.get(reverse('tour:my_tour'))
        self.assertEqual(response.status_code, 302)

    def test_view_tour_view(self):
        c = Client()
        tour = Tour.objects.first()
        user = User.objects.get(username='user2')
        check_owner = 0
        c.force_login(user)
        check_owner = 1
        self.assertEqual(check_owner, 1)
        response = c.get(reverse('tour:view_tour', args=(tour.id,)))
        self.assertEqual(response.status_code, 200)

    def test_update_tour_view_success(self):
        c = Client()
        this_tour = Tour.objects.first()
        check_update = 1

        initial_data = {
            't_title': this_tour.t_name,
            'province': this_tour.province,
            'amount': this_tour.amount,
            'period': this_tour.period,
            'img': this_tour.img,
            'information': this_tour.information,
        }

        user = User.objects.get(username='user2')
        c.force_login(user)

        response = c.get(reverse('tour:update_tour', args=(this_tour.id,)))
        self.assertEqual(response.status_code, 200)

    def test_update_tour_view_unsuccess(self):
        c = Client()
        this_tour = Tour.objects.first()
        user = User.objects.get(username='user3')
        c.force_login(user)
        response = c.get(reverse('tour:update_tour', args=(this_tour.id,)))
        self.assertEqual(response.status_code, 302)

    def test_remove_tour_success(self):
        c = Client()
        tour = Tour.objects.first()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('tour:remove_tour', args=(tour.id,)))
        self.assertEqual(response.status_code, 302)

    def test_remove_tour_unsuccess(self):
        c = Client()
        tour = Tour.objects.first()
        user = User.objects.get(username='user3')
        c.force_login(user)
        response = c.get(reverse('tour:remove_tour', args=(tour.id,)))
        self.assertEqual(response.status_code, 302)

    def test_home_view(self):
        c = Client()
        tour = Tour.objects.all()
        response = c.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        c = Client()
        response = c.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)
