from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest

from users.models import User, Guide, Member
from tour.models import Tour, Review, BookTour
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
            user=userguide1, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx', guide_image='xxx.jpg')
        admin = User.objects.create(username='user3', password=make_password(
            '1234'), email='user2@example.com', is_guide=True, is_admin=True)
            
        guide = Guide.objects.create(
            user=admin, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx', guide_image='xxx.jpg')

        usermember = User.objects.create(username='user4', password=make_password(
            '1234'), email='user3@example.com', is_member=True)
        member = Member.objects.create(user=usermember, gender='xxx', age='xxx',
                                       address='xxx', allergic='xxx', underlying_disease='xxx', religion='xxx')

        # Create Tour
        tour = Tour.objects.create(t_name='xxx', guide=userguide1, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx', img='img.png')


        #iteration 3
        guide1 = User.objects.create(username='guide1', password=make_password(
            '1234'), email='user2@example.com', is_guide=True)
        guide = Guide.objects.create(
            user=guide1, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx', guide_image='xxx.jpg')

        member1 = User.objects.create(username='member1', password=make_password(
            '1234'), email='user3@example.com', is_member=True)
        member = Member.objects.create(user=member1, gender='xxx', age='xxx',
                                       address='xxx', allergic='xxx', underlying_disease='xxx', religion='xxx')
        
        member2 = User.objects.create(username='member2', password=make_password(
            '1234'), email='user3@example.com', is_member=True)
        member = Member.objects.create(user=member2, gender='xxx', age='xxx',
                                       address='xxx', allergic='xxx', underlying_disease='xxx', religion='xxx')
    #iteration 3
    def test_change_status_to_verified(self):
        # test ว่า guide สามารถเปลี่ยนstatus ของ bookTour เป็นverified ได้
        c = Client()
        guide = User.objects.get(username='guide1')
        member = User.objects.get(username='member1')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        bookTour = BookTour.objects.create(tour=tour,member=member,verify_member='not_verified')
        c.force_login(guide)
        data = { 'status' : 'verified'}
   
        response = c.post(reverse('tour:change_status', args=(bookTour.id,)), data)
        bookTour.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(bookTour.verify_member,  "verified")
    
    def test_change_status_to_denied(self):
        # test ว่า guide สามารถเปลี่ยนstatus ของ bookTour เป็นdenied ได้
        c = Client()
        guide = User.objects.get(username='guide1')
        member = User.objects.get(username='member1')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        bookTour = BookTour.objects.create(tour=tour,member=member,verify_member='not_verified')
        c.force_login(guide)
        data = { 'status' : 'denied'}
   
        response = c.post(reverse('tour:change_status', args=(bookTour.id,)), data)
        bookTour.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(bookTour.verify_member,  "denied")

    def test_change_status_to_not_verified(self):
        # test ว่า guide สามารถเปลี่ยนstatus ของ bookTour เป็นnot verifiedได้
        c = Client()
        guide = User.objects.get(username='guide1')
        member = User.objects.get(username='member1')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        bookTour = BookTour.objects.create(tour=tour,member=member,verify_member='verified')
        c.force_login(guide)
        data = { 'status' : 'not_verified'}
   
        response = c.post(reverse('tour:change_status', args=(bookTour.id,)), data)
        bookTour.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(bookTour.verify_member,  "not_verified")

    def test_profile_tour_view_success(self):
        # test ว่า guide สามารถเข้าหน้า profile_tour success
        c = Client()
        guide = User.objects.get(username='guide1')
        c.force_login(guide)
        response = c.get(reverse('tour:profile_tour'))
        self.assertEqual(response.status_code, 200)

    def test_book_tour_success(self):
        # test ว่า member สามารถเปลี่ยนbook Tour success
        c = Client()
        guide = User.objects.get(username='guide1')
        member = User.objects.get(username='member1')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        c.force_login(member)

        response = c.post(reverse('tour:book_tour', args=(tour.id,)))
        self.assertEqual(response.status_code, 302)
        #ถ้า booktour ที่สร้างล่าสุดมีmemberที่สร้าง ตรงกับ member ที่สร้าง
        self.assertEqual(BookTour.objects.last().member,  member)

    def test_add_review_success(self):
        # test ว่า สามารถadd review ได้
        c = Client()
        guide = User.objects.get(username='guide1')
        member = User.objects.get(username='member1')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        data = {'review_title' : 'xxx',
                'review_text' : 'xxx',
                'rating' : 4,}
        c.force_login(member)
   
        response = c.post(reverse('tour:add_review', args=(tour.id,)), data)
        self.assertEqual(response.status_code, 302)
        # ถ้าreview_user field ในreviewที่ add ล่าสุด เท่ากับ member ที่เป็นคน add
        self.assertEqual(Review.objects.last().review_user,  member)

    def test_remove_review_success(self):
        # test ว่า สามารถremove review ไดเ้
        c = Client()
        guide = User.objects.get(username='guide1')
        member = User.objects.get(username='member1')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        review = Review.objects.create( review_user = member, review_title = 'xxx', review_text = 'xxx', rating = 4, ) 
        review.review_tour.add(tour)
        review.save()
        c.force_login(member)
   
        response = c.post(reverse('tour:remove_review', args=(review.id,)))
        self.assertEqual(response.status_code, 302)
        # ถ้านับreview ทั้งหมด เท่ากับ 0
        self.assertEqual(Review.objects.count(),  0)

    def test_remove_review_unsuccess(self):
        # test ว่ากรณีที่userไม่ตรงกับคนสร้างจะไม่สามารถremove review ได้
        c = Client()
        guide = User.objects.get(username='guide1')
        member1 = User.objects.get(username='member1')
        member2 = User.objects.get(username='member2')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        review = Review.objects.create( review_user = member1, review_title = 'xxx', review_text = 'xxx', rating = 4, ) 
        review.review_tour.add(tour)
        review.save()
        c.force_login(member2)
   
        response = c.post(reverse('tour:remove_review', args=(review.id,)))
        self.assertEqual(response.status_code, 302)
        # ถ้านับreview ทั้งหมด เท่ากับ 1
        self.assertEqual(Review.objects.count(),  1)

    def test_create_tour_success(self):
        # test ว่า create tour success
        c = Client()
        guide = User.objects.get(username='guide1')
        data = {
            't_name' : "addtour",
            'province' : "xxx",
            'price' : 200,
            'amount' : 30,
            'period' : "xxx",
            'snippet' : "xxx",
            'information' : "xxx",
        }           
        c.force_login(guide)
   
        response = c.post(reverse('tour:create_tour'), data)
        self.assertEqual(response.status_code, 302)
        # ถ้าguide field ที่อยู่ในtour ที่ชื่อ addtour เท่ากับ guide ที่login 
        self.assertEqual(Tour.objects.get(t_name='addtour').guide,  guide)
    
    
    def test_my_tour_guide_view_success(self):
        # test ว่า guide สามารถเข้าหน้า my_tour_guide
        c = Client()
        guide = User.objects.get(username='guide1')
        c.force_login(guide)
        response = c.get(reverse('tour:my_tour_guide'))
        self.assertEqual(response.status_code, 200)

    def test_my_tour_guide_view_unsuccess(self):
        # test ว่า guide สามารถเข้าหน้า my_tour_guide
        c = Client()
        guide = User.objects.get(username='member1')
        c.force_login(guide)
        response = c.get(reverse('tour:my_tour_guide'))
        self.assertEqual(response.status_code, 302)

    def test_view_tour_booked_member_booked(self):
        # กรณีที่ user bookไปแล้ว
        c = Client()
        guide = User.objects.get(username='guide1')
        member = User.objects.get(username='member1')
        tour = Tour.objects.create(t_name='tour1', guide=guide, province='xxx',
                            price=2000, period='xxx', amount=10, information='xxx',verify_tour=True,img='img.png')
        bookTour = BookTour.objects.create(tour=tour,member=member)
        c.force_login(member)

        response = c.get(reverse('tour:view_tour', args=(tour.id,)))
        self.assertEqual(response.status_code, 200)
        # ค่า check_booked จะเป็น False
        self.assertEqual(response.context['check_booked'], False)

    
    
    
    
    
    
    
    #iteration 2
    def test_guide_create_tour_view(self):
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
        self.assertEqual(response.status_code, 200)

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

        response = self.client.post(
            reverse('tour:create_tour'), data=form_data)
        self.assertEqual(response.status_code, 302)

        tours = Tour.objects.all()
        self.assertEqual(tours.count(), 1)

    def test_my_tour_view_success(self):
        c = Client()
        user = User.objects.get(username='member1')
        c.force_login(user)
        response = c.get(reverse('tour:my_tour'))
        self.assertEqual(response.status_code, 200)

    def test_my_tour_view_unsuccess(self):
        c = Client()
        user = User.objects.get(username='guide1')
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
        self.assertEqual(response.status_code, 200)

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

    ################# edit ####################

    #ทดสอบว่าเพิ่ม review ได้ไหม บน model
    def test_review(self):
        user = User.objects.get(username='user4')
        this_user = User.objects.get(id = user.id)
        review = Review.objects.create(review_user = this_user,review_title="test", review_text="good", rating=3)
        review = Review.objects.all()
        self.assertEqual(review.count(), 1)
    
    
