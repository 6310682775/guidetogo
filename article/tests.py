from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.test import TestCase, Client
from article.views import LikeView, CategoryView, ArticleHome, ArticleDetail, AddArticle, AddCategory, UpdateArticle ,DeleteArticle
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest
from article.models import Article, Category
from users.models import User, Guide, Member
# Create your tests here.
# class TestUrls(SimpleTestCase):

#     def test_article_home_url_is_resolved(self):
#         url = reverse('article:article_home')
#         self.assertEqual(resolve(url).func, ArticleHome)
    
#     def test_article_detail_url_is_resolved(self):
#         url = reverse('article:article_detail')
#         self.assertEqual(resolve(url).func, ArticleDetail)

#     def test_article_add_url_is_resolved(self):
#         url = reverse('article:article_add')
#         self.assertEqual(resolve(url).func, AddArticle)

#     def test_category_add_is_resolved(self):
#         url = reverse('article:category_add')
#         self.assertEqual(resolve(url).func, AddCategory)
    
#     def test_category_view_url_is_resolved(self):
#         url = reverse('article:category_view', args=['food'])
#         self.assertEqual(resolve(url).func, CategoryView)
    
#     def test_article_update_url_is_resolved(self):
#         url = reverse('article:article_update', args=['1'])
#         self.assertEqual(resolve(url).func, UpdateArticle)
    
#     def test_article_delete_url_is_resolved(self):
#         url = reverse('article:article_delete', args=['1'])
#         self.assertEqual(resolve(url).func, DeleteArticle)
    
#     def test_like_article_url_is_resolved(self):
#         url = reverse('article:like_article', args=['1'])
#         self.assertEqual(resolve(url).func, LikeView)


class TestViews(TestCase):
    def setUp(self):
        
        User.objects.create(username='user1', password=make_password(
            '1234'), email='user1@example.com')

        userguide1 = User.objects.create(username='user2', password=make_password(
            '1234'), email='user2@example.com', is_guide=True)
        guide = Guide.objects.create(
            user=userguide1, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx')
        admin = User.objects.create(username='admin', password=make_password(
            '1234'), email='user2@example.com', is_admin=True)
        guide = Guide.objects.create(
            user=admin, gender='xxx', age='xxx', province='xxx', address='xxx', tat_license='xxx')

        usermember = User.objects.create(username='user4', password=make_password(
            '1234'), email='user3@example.com', is_member=True)
        member = Member.objects.create(user=usermember, gender='xxx', age='xxx', address='xxx', allergic='xxx', underlying_disease = 'xxx', religion = 'xxx')
        article1 = Article.objects.create(title = 'article1',author =userguide1,category = 'xxx',snippet = 'xxx')
        category = Category.objects.create(name = 'category1')
        article2 = Article.objects.create(title = 'article2',author =userguide1,category = 'xxx',snippet = 'xxx')
        

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
        # test ว่าสามารถเข้าหน้า detailของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_detail', args=str(article.id)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_detail.html')

    def test_article_add_home_GET(self):
        # test ว่าสามารถเข้าหน้า detailของ article
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
    
    def test_category_view_GET(self):
        # test ว่าสามารถเข้าหน้า detailของ article
        c = Client()
        user = User.objects.get(username='user2')
        category = Category.objects.get(name='category1')
        c.force_login(user)
        response = c.get(reverse('article:category_view', args=[str(category.name)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/category.html')

    def test_article_update_GET(self):
        # test ว่าสามารถเข้าหน้า detailของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_update', args=[str(article.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_update.html')
    
    def test_article_delete_GET(self):
        # test ว่าสามารถเข้าหน้า detailของ article
        c = Client()
        user = User.objects.get(username='user2')
        article = Article.objects.get(title='article1')
        c.force_login(user)
        response = c.get(reverse('article:article_delete', args=[str(article.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article/article_delete.html')

    def test_AddArticle_GET(self):
        # test ว่าสามารถadd article ได้ไหม
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


    def test_UpdateArticle_GET(self):
        # test ว่าสามารถ update article ได้ไหม
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

    def test_LikeView_GET(self):
        # test ว่าสามารถ add category ได้ไหม
        c = Client()
        user = User.objects.get(username='admin')
        article = Article.objects.get(title='article2')
        c.force_login(user)
        response = c.post(reverse('article:like_article', args=[str(article.pk)] ))
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.likes.count(),  1)

    def test_DeleteArticle_GET(self):
        # test ว่าสามารถ update article ได้ไหม
        c = Client()
        user = User.objects.get(username='admin')
        article = Article.objects.get(title='article2')
        c.force_login(user)
        response = c.post(reverse('article:article_delete', args=[str(article.id)] ))

        article = Article.objects.all()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.count(),  1)

    def test_AddCategory_GET(self):
        # test ว่าสามารถ add category ได้ไหม
        form_data = {
            'name' : "AddCategory"
        }
        c = Client()
        user = User.objects.get(username='admin')
        c.force_login(user)
        response = c.post(reverse('article:category_add'), data = form_data)

        category = Category.objects.last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(category.name,  "AddCategory")
    
    