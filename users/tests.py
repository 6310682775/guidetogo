from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import User, Member, Guide
from .forms import MemberSignUpForm, GuideSignUpForm

from django.core.files.uploadedfile import InMemoryUploadedFile
from io import StringIO
import base64               # for decoding base64 image
import tempfile             # for setting up tempdir for media
from django.test import TestCase, override_settings

# Create your tests here.


class UserViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="user1", password=make_password(
            '1234'), email="user1@example.com")
        userguide = User.objects.create(username="user2", password=make_password(
            '1234'), email="user2@example.com", is_guide=True)
        guide = Guide.objects.create(
            user=userguide, phone_number="0927866309", detail="xxx", gender="Male", age="20", email="6310611006@student.tu.ac.th", address="xxx", province="xxx", tat_license="xxx", guide_image="xxx.jpg")
        usermem = User.objects.create(username="user3", password=make_password(
            '1234'), email="user2@example.com", is_member=True)
        mem = Member.objects.create(
            user=usermem, phone_number="0927866309", gender="Male", age="22", email="6310611007@student.tu.ac.th", address="xxx", allergic="xxx", underlying_disease="xxx", religion="xxx", member_image="xxx.jpg",)
    # ทดสอบหน้า login

    def test_login_view_with_authentication(self):
        c = Client()
        user = User.objects.get(username="user1")
        c.force_login(user)
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 302)
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
    # ทดสอบ logout

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
        user = User.objects.get(username='user3')
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
        # override settings for media dir to avoid filling up your disk
        @override_settings(MEDIA_ROOT=tempfile.gettempdir())
        def test_valid(self):
            from django.core.files.uploadedfile import InMemoryUploadedFile
            # StringIO and BytesIO are parts of io module in python3
            from io import BytesIO
            image = InMemoryUploadedFile(
                BytesIO(base64.b64decode("media/images/member/2.jpg")
                        ),            # use io.BytesIO
                field_name='tempfile',
                name='tempfile.png',
                content_type='image/png',
                size=len("media/images/member/2.jpg"),
                charset='utf-8',
            )
            response = self.client.post(reverse('users:guide_register'), data={
                "username": "user4",
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
                "guide_image": image,
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
            "guide_image": "xxx.jpg"
        })
        self.assertEqual(response.status_code, 200)

        users = Guide.objects.all()
        self.assertEqual(users.count(), 1)

    def test_member_signup_form(self):
        # override settings for media dir to avoid filling up your disk
        @override_settings(MEDIA_ROOT=tempfile.gettempdir())
        def test_valid(self):
            from django.core.files.uploadedfile import InMemoryUploadedFile
            # StringIO and BytesIO are parts of io module in python3
            from io import BytesIO
            image = InMemoryUploadedFile(
                # use io.BytesIO
                BytesIO(base64.b64decode("media/images/member/26622.jpg")),
                field_name='tempfile',
                name='tempfile.png',
                content_type='image/png',
                size=len("media/images/member/26622.jpg"),
                charset='utf-8',
            )
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
                "member_image": image
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



    # ทดสอบ member สามารถ edit profile member สำเร็จ
    def test_member_profile_edit_successful(self):
        user = User.objects.get(username='user3')
        mem = Member.objects.first()

        c = Client()
        c.force_login(user)
        response = c.post(reverse('users:member_profile_edit'), {
            'user': user,
            'phone_number': '0927866309',
            'age': '20',
            'allergic': 'xxx',
            'address': 'xxx',
            'underlying_disease': 'xxx',
            'religion': 'xxx',
        })
        self.assertEqual(response.status_code, 302)

    # ทดสอบ member สามารถ edit profile member ไม่สำเร็จ
    def test_member_profile_edit_unsuccessful(self):
        user = User.objects.get(username='user3')
        mem = Member.objects.first()

        c = Client()
        c.force_login(user)
        response = c.post(reverse('users:member_profile_edit'), {
            'user': user,
            'phone_number': '0927866309',
            'age': '20',
            'allergic': 'xxx',
            'address': 'xxx',
            'underlying_disease': 'xxx',
            
        })
        self.assertEqual(response.status_code, 200)

    # ทดสอบ guide สามารถ edit profile guide สำเร็จ
    def test_guide_profile_edit_successful(self):
        user = User.objects.get(username='user2')
        guide = Guide.objects.first()

        c = Client()
        c.force_login(user)
        response = c.post(reverse('users:guide_profile_edit'), {
            'user': user,
            'detail': 'i love thailand',
            'phone_number': '191',
            'age': '20',
            'email': 'test@example.com',
        })
        self.assertEqual(response.status_code, 302)

    # ทดสอบ guide สามารถ edit profile guide ไม่สำเร็จ
    def test_guide_profile_edit_unsuccessful(self):
        user = User.objects.get(username='user2')
        guide = Guide.objects.first()

        c = Client()
        c.force_login(user)
        response = c.post(reverse('users:guide_profile_edit'), {
            'user': user,
            'detail': 'i love thailand',
            'phone_number': '191',
            'age': '20',
            'email': 'test',
        })
        self.assertEqual(response.status_code, 200)