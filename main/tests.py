from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from main.filters import Tourfilter
from users.models import User, Guide, Member
from tour.models import Tour, Review
from tour.forms import TourForm
import django_filters
from django_filters.exceptions import FieldLookupError
from django.db import models
from django_filters import LookupChoiceFilter, CharFilter
from django import forms


# Create your tests here.
class TourSearchListViewTest(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

        test_author = User.objects.create(username="user1", password=make_password(
            '1234'), email="user1@example.com", first_name='John', last_name='Smith')
        userguide1 = User.objects.create(username='user2', password=make_password(
            '1234'), email='user2@example.com', is_guide=True)

        Tour.objects.create(guide=userguide1, province='Ayutthaya',
                            price=2000, period='5', amount=5, information='xxx1', img='img1.png')
        Tour.objects.create(t_name='xxx2', guide=userguide1, province='Bueng Kan',
                            price=5000, period='10', amount=10, information='xxx2', img='img2.png')
        Tour.objects.create(t_name='xxx3', guide=userguide1, province='Ratchaburi',
                            price=10000, period='7', amount=15, information='xxx3', img='img3.png')

    #ทดสอบการเข้าถึงหน้า home
    def test_django_filters(self):
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        
        response = c.get(
            reverse('main:home'))
        self.assertEqual(response.status_code, 200)

    # ทดสอบการเข้าถึงหน้า about
    def test_about_view(self):
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('main:about'))
        self.assertEqual(response.status_code, 200)


    # ทดสอบการประกาศ filter เเละ ทดสอบว่า filters ได้รับ model จะได้เป็นจำนวนที่ประกาศเเละ จำนวน field ของ models ที่ filters ได้รับ
    def test_declared_and_model_derived(self):
        class F(django_filters.FilterSet):
            price = django_filters.LookupChoiceFilter(
                field_class=forms.DecimalField,
                lookup_choices=[
                    ('exact', 'Equals'),
                    ('gt', 'Greater than'),
                    ('lt', 'Less than'),
                ]
            )
            period = django_filters.LookupChoiceFilter(
                field_class=forms.DecimalField,
                lookup_choices=[
                    ('exact', 'Equals'),
                    ('gt', 'Greater than'),
                    ('lt', 'Less than'),
                ]
            )
            amount = django_filters.LookupChoiceFilter(
                field_class=forms.DecimalField,
                lookup_choices=[
                    ('exact', 'Equals'),
                    ('gt', 'Greater than'),
                    ('lt', 'Less than'),
                ]
            )

            class Meta:
                model = Tour
                fields = ('__all__')
                filter_overrides = {
                    models.ImageField: {
                        'filter_class': django_filters.CharFilter,
                        'extra': lambda f: {
                            'img': 'icontains',
                        },
                    },
                }
        self.assertEqual(len(F.declared_filters), 3)
        self.assertEqual(len(F.base_filters), 12)
        self.assertListEqual(
            list(F.base_filters), ["t_name", "guide", "province", "price",
                                   "period", "amount", "snippet", "information", "img", "review", "date", "status"]
        )
