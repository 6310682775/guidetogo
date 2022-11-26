from django import forms
from .models import Article,Category
from django.db import transaction

def category_choice():
    if Category.objects.all().exists():
        choices = Category.objects.all().values_list('name','name')

        choices_List = []

        for item in choices:
            choices_List.append(item)
        
        return choices_List
    else:
        return  []

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        category=[
            ('HOTEL','HOTEL'),
            ('CAFE','CAFE'),
            ('NATURAL','NATURAL'),
            ('LANDMARK','LANDMARK'),
            ('BEACH','BEACH'),
            ('MOUNTAIN','MOUNTAIN'),
            ('CAMPING','CAMPING'),
            ('FOREST','FOREST'),
            ('TOUR','TOUR'),
            ('PARTY','PARTY'),
            ('FAMILY','FAMILY'),
        ]

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

        category=[
            ('HOTEL','HOTEL'),
            ('CAFE','CAFE'),
            ('NATURAL','NATURAL'),
            ('LANDMARK','LANDMARK'),
            ('BEACH','BEACH'),
            ('MOUNTAIN','MOUNTAIN'),
            ('CAMPING','CAMPING'),
            ('FOREST','FOREST'),
            ('TOUR','TOUR'),
            ('PARTY','PARTY'),
            ('FAMILY','FAMILY'),
        ]
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=category,attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

        
