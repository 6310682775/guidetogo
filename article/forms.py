from django import forms
from .models import Article,Category
from django.db import transaction


choices = Category.objects.all().values_list('name','name')

choices_List = []

for item in choices:
    choices_List.append(item)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','category', 'body','snippet','article_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'this is placeholder'}),
            'category' : forms.Select(choices=choices_List,attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
    
        }



class UpdateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','category','body','snippet','article_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'this is placeholder'}),
            'category' : forms.Select(choices=choices_List,attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }
