from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import TestCase, Client
from article.views import LikeView, CategoryView, ArticleHome, ArticleDetail, AddArticle, UpdateArticle ,DeleteArticle
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from article.models import Article
from users.models import User, Guide, Member
# Create your tests here.

class TestViews(TestCase):
    def setUp(self):
        
        # Create user guide
        userguide1 = User.objects.create(username='user2', password=make_password(
            '1234'), email='user2@example.com', is_guide=True)
        guide = Guide.objects.create(
            user=userguide1, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx',guide_image='xxx.jpg')

        # Create user admin
        admin = User.objects.create(username='admin', password=make_password(
            '1234'), email='user2@example.com', is_admin=True)
        guide = Guide.objects.create(
            user=admin, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx')

        # Create user member
        usermember = User.objects.create(username='user4', password=make_password(
            '1234'), email='user3@example.com', is_member=True)
        member = Member.objects.create(user=usermember, gender='xxx', age='xxx', address='xxx', allergic='xxx', underlying_disease = 'xxx', religion = 'xxx')

        # Create 2 article
        article1 = Article.objects.create(title = 'article1',author =userguide1,category = 'xxx',snippet = 'xxx')
        article2 = Article.objects.create(title = 'article2',author =userguide1,category = 'xxx',snippet = 'xxx')

        # Create 1 category

        

    def test_article_home_GET(self):
        # เข้าหน้าhome tour ได้
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('article:article_home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_home.html')

    def test_article_detail_GET(self):
        # test ว่าสามารถเข้าหน้า detailของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_detail', args=str(article.id)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_detail.html')
    

    def test_article_detail_GET(self):
        # test ว่าสามารถเข้าหน้า detail ของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_detail', args=str(article.id)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_detail.html')

    #iteration 3
    def test_article_detail_Liked_GET(self):
        # test ว่าสามารถเข้าหน้า detail ของ article กรณีที่ user คนนั้น like article นั้นแล้ว
        c = Client()
        member = User.objects.get(username='user4')
        article = Article.objects.get(title='article1')
        article.likes.add(member)
        article.save()
        c.force_login(member)
        response = c.get(reverse('article:article_detail', args=str(article.id)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_detail.html')
        self.assertEqual(response.context['liked'], True)

    def test_article_add_home_GET(self):
        # test ว่าสามารถเข้าหน้า detail ของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_add.html')

    def test_category_add_GET(self):
        # test ว่าสามารถเข้าหน้า detailของ article
        c = Client()
        user = User.objects.get(username='user2')
        c.force_login(user)
        response = c.get(reverse('article:category_add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/category_add.html')
    
    # def test_category_view_GET(self):
    #     # test ว่าสามารถเข้าหน้า detailของ article
    #     c = Client()
    #     user = User.objects.get(username='user2')
    #     category = Category.objects.get(name='category1')
    #     c.force_login(user)
    #     response = c.get(reverse('article:category_view', args=[str(category.name)]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'article/category.html')

    def test_article_update_GET(self):
        # test ว่าสามารถเข้าหน้า update ของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_update', args=[str(article.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_update.html')
    
    def test_article_delete_GET(self):
        # test ว่าสามารถเข้าหน้า delete ของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_delete', args=[str(article.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_delete.html')

    def test_AddArticle_success(self):
        # test ว่าสามารถ add article ได้ไหม
        form_data = {
            'title' : "AddArticle",
            'category' : "xxx",
            'snippet' : "xxx",
            'body' : "xxx",
        }
        c = Client()
        user = User.objects.get(username='admin')
        c.force_login(user)
        response = c.post(reverse('article:article_add'), data = form_data)

        article = Article.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.title,  "AddArticle")


    def test_UpdateArticle_success(self):
        # test ว่าสามารถ update article ได้
        form_data = {
            'title' : "UpdateArticle",
            'category' : "xxx",
            'snippet' : "xxx",
            'body' : "xxx",
        }
        c = Client()
        user = User.objects.get(username='admin')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.post(reverse('article:article_update', args=[str(article.id)] ), data = form_data)

        article = Article.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.title,  "UpdateArticle")


    #iteration 3
    def test_LikeView_like_success(self):
        # testว่าสามารถlike ได้

        c = Client()
        member = User.objects.get(username='user4')
        article = Article.objects.get(title='article2')
        data = {'article_id': article.id}
        c.force_login(member)
        
        response = c.post(reverse('article:like_article', args=(member.id,)), data)
        
        article.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.likes.count(),  1)

    #iteration 3
    def test_LikeView_unlike_success(self):
        # testว่าสามารถ unlike ได้
        c = Client()
        member = User.objects.get(username='user4')
        article = Article.objects.get(title='article2')
        article.likes.add(member)
        article.save()
        data = {'article_id': article.id}
        c.force_login(member)
        
        response = c.post(reverse('article:like_article', args=(member.id,)), data)
        
        article.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.likes.count(),  0)

    def test_DeleteArticle_success(self):
        # test ว่าสามารถ Delete article ได้
        c = Client()
        user = User.objects.get(username='admin')
        article = Article.objects.get(title='article2')
        c.force_login(user)
        response = c.post(reverse('article:article_delete', args=[str(article.id)] ))

        article = Article.objects.all()
        self.assertEqual(response.status_code, 302)
        # จากเริ่มต้นมี 2article ถูก delete จึงเหลือ 1
        self.assertEqual(article.count(),  1)

    # def test_AddCategory_success(self):
    #     # test ว่าสามารถ add category ได้
    #     form_data = {
    #         'name' : "AddCategory"
    #     }
    #     c = Client()
    #     user = User.objects.get(username='admin')
    #     c.force_login(user)
    #     response = c.post(reverse('article:category_add'), data = form_data)

    #     category = Category.objects.last()
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(category.name,  "AddCategory")
    
    