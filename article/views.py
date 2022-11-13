from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ArticleForm, UpdateArticleForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# # Create your views here.
# def article_home(request):
#     return render(request, 'article/article_home.html', {})


def LikeView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    article.likes.add(request.user)
    return HttpResponseRedirect(reverse("article:article_detail", args=[str(pk)]))

class ArticleHome(ListView):
    model = Article
    template_name = "article/article_home.html"
    ordering = ['-post_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.all()
        context['category'] = category
        return context


    

def CategoryView(request, cats):
    category_posts = Article.objects.filter(category=cats)
    category = Category.objects.all()
    return render(request, 'article/category.html', {'cats':cats, 'category_posts':category_posts, 'category':category})

class ArticleDetail(DetailView):
    model = Article
    template_name = "article/article_detail.html"

    def get_context_data(self, *arg,**kwargs):
        context = super(ArticleDetail, self).get_context_data(*arg,**kwargs)
        stuff = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        category = Category.objects.all()
        context['category'] = category
        context["total_likes"] = total_likes
        return context

class AddArticle(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "article/article_add.html"
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCategory(LoginRequiredMixin, CreateView):
    model = Category
    # form_class = ArticleForm
    template_name = "article/category_add.html"
    fields = '__all__'

class UpdateArticle(UpdateView):
    model = Article
    form_class = UpdateArticleForm
    template_name = 'article/article_update.html'
    # fields = ['title', 'body']

class DeleteArticle(DeleteView):
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('article:article_home')