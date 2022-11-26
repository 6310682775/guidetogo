from django import forms
from .models import Article,Category
from django.db import transaction

# def category_choice():
#     choices = Category.objects.all().values_list('name','name')

#     choices_List = []

#     for item in choices:
#         choices_List.append(item)
    
#     return choices_List

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','category', 'body','snippet','article_image')

        category = Category.category_choice()
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=category,attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
    
        }



class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','category','body','snippet','article_image')

        category = Category.category_choice()
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=category,attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
