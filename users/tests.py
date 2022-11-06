from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import User, Member, Guide
from .form import MemberSignUpForm, GuideSignUpForm

# Create your tests here.


class UserViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="user1", password=make_password(
            '1234'), email="user1@example.com")
        userguide = User.objects.create(username="user2", password=make_password(
            '1234'), email="user2@example.com", is_guide=True)
        guide = Guide.objects.create(
            user = userguide, phone_number = "0927866309", detail = "xxx", gender  = "Male", age = "20", email = "6310611006@student.tu.ac.th", address = "xxx", province = "xxx", tat_license = "xxx", guide_image = "xxx.jpg")
        usermem = User.objects.create(username="user3", password=make_password(
            '1234'), email="user2@example.com", is_member=True)
        mem = Member.objects.create(
            user = usermem, phone_number = "0927866309", gender  = "Male", age = "22", email = "6310611007@student.tu.ac.th", address = "xxx", allergic = "xxx", underlying_disease = "xxx", religion = "xxx")
    # ทดสอบหน้า lohin
    def test_login_view_with_authentication(self):  
        c = Client()
        user = User.objects.get(username="user1")
        c.force_login(user)
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
    # ทดสอบหน้า login
    def test_login_view_without_authentication(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
    # ทดสอบว่าล็อกอินสำเร็จ
    def test_login_success(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.post(reverse('users:login'), {
                          'username': 'user1', 'password': '1234'})
        self.assertEqual(response.status_code, 302)
    # ทดสอบล็อกอินไม่สำเร็จ
    def test_login_unsuccess(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.post(reverse('users:login'), {
                          'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)
    #ทดสอบ logout
    def test_logout_success(self):
        c = Client()
        user = User.objects.get(username="user1")
        c.force_login(user)
        response = c.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
    
    def test_member_view_without_auth(self):
        user = User.objects.get(username='user1')
        c = Client()
        response = c.get(reverse('users:member_profile'))
        self.assertEqual(response.status_code, 302)

    def test_member_view_with_auth(self):
        user = User.objects.get(username='user1')
        c = Client()
        c.force_login(user)
        response = c.get(reverse('users:member_profile'))
        self.assertEqual(response.status_code, 200)

    def test_guide_view_without_auth(self):
        user = User.objects.get(username='user1')
        c = Client()
        response = c.get(reverse('users:guide_profile'))
        self.assertEqual(response.status_code, 302)

    def test_guide_view_with_auth(self):
        userguide = User.objects.get(username='user2')
        c = Client()
        c.force_login(userguide)
        response = c.get(reverse('users:guide_profile'), args=(userguide.id,))
        self.assertEqual(response.status_code, 200)

    def test_guide_signup_form(self):
        response = self.client.post(reverse('users:guide_register'), data={
            "username": "test1",
            "password1": "Awd234523",
            "password2": "Awd234523",
            "first_name": "john",
            "last_name": "wick",
            "email": "test1@hotmail.com",
            "age": "20",
            "phone_number": "123456789",
            "address": "xxx",
            "gender": "Male",
            "detail": "xxx",
            "province": "xxx",
            "tat_license": "xxx1234",
            "guide_image": "xxx"
        })
        self.assertEqual(response.status_code, 302)

        users = Guide.objects.all()
        self.assertEqual(users.count(), 2)

    def test_guide_cannot_signup_form(self):
        response = self.client.post(reverse('users:guide_register'), data={
            "username": "",
            "password1": "",
            "password2": "",
            "first_name": "john",
            "last_name": "wick",
            "email": "test1@hotmail.com",
            "age": "20",
            "phone_number": "123456789",
            "address": "xxx",
            "gender": "Male",
            "detail": "xxx",
            "province": "xxx",
            "tat_license": "xxx1234",
            "guide_image": "xxx"
        })
        self.assertEqual(response.status_code, 200)

        users = Guide.objects.all()
        self.assertEqual(users.count(), 1)


    def test_member_signup_form(self):
        response = self.client.post(reverse('users:member_register'), data={
            "username": "test1",
            "password1": "Awd234523",
            "password2": "Awd234523",
            "first_name": "john",
            "last_name": "wick",
            "email": "test1@hotmail.com",
            "age": "20",
            "phone_number": "123456789",
            "address": "xxx",
            "gender": "Male",
            "allergic": "xxx",
            "religion": "xxx",
            "underlying_disease": "xxx",
            "member_image": "xxx"
        })
        self.assertEqual(response.status_code, 302)

        users = Member.objects.all()
        self.assertEqual(users.count(), 2)

    def test_member_cannot_signup_form(self):
        response = self.client.post(reverse('users:member_register'), data={
            "username": "",
            "password1": "",
            "password2": "",
            "first_name": "john",
            "last_name": "wick",
            "email": "test1@hotmail.com",
            "age": "20",
            "phone_number": "123456789",
            "address": "xxx",
            "gender": "Male",
            "allergic": "xxx",
            "religion": "xxx",
            "underlying_disease": "xxx",
            "member_image": "xxx"
        })
        self.assertEqual(response.status_code, 200)

        users = Member.objects.all()
        self.assertEqual(users.count(), 1)

'''
    def test_register_page_form(self):
        c = Client()
        form_data = {
            "username": "kik1239",
            "email": "first123456@hotmail.com",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "ariya",
            "last_name": "woddw"}
        form = MemberSignUpForm(data=form_data)
        response = c.post(reverse('Users:register'), {
            "username": "kik1239",
            "email": "",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "ariya",
            "last_name": "woddw"}, follow=True)
        self.assertEqual(response.status_code, 200)'''
"""
    def test_favourite_add_successful(self):
        user1 = User.objects.get(username='user1')
        userstore = User.objects.get(username="user2")
        store = Store.objects.first()
        c = Client()
        c.force_login(user1)
        response = c.get(reverse('users:favourite', args=("2")))
        self.assertEqual(store.favourite.count(), 1)


    def test_favourite_remove_successful(self):
        user1 = User.objects.get(username='user1')
        userstore = User.objects.get(username="user2")
        store = Store.objects.first()
        store.favourite.add(user1)
        c = Client()
        c.force_login(user1)
        response = c.get(reverse('users:favourite', args=("2")))
        self.assertEqual(store.favourite.count(), 0)


    def test_favourite_view(self):
        user = User.objects.get(username='user1')
        c = Client()
        c.force_login(user)
        response = c.get(reverse('users:favourite_view', args=(user.id,)))
        self.assertEqual(response.status_code, 200)

    def test_customer_profile_successful(self):
        user = User.objects.get(username='user3')
        cus = Customer.objects.first()

        c = Client()
        c.force_login(user)
        response = c.post(reverse('users:customer_profile'), {
            'user': user, 'first_name': 'kkk',
        })
        self.assertEqual(response.status_code, 200)

    def test_store_profile_successful(self):
        userstore = User.objects.get(username="user2")
        store = Store.objects.first()

        c = Client()
        c.force_login(userstore)
        response = c.post(reverse('users:store_profile'), {
            'user': userstore ,'store_name': 'kkk',
        })
        self.assertEqual(response.status_code, 200)
        """