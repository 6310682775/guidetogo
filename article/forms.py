from django import forms
from .models import Article
from django.db import transaction



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','category','snippet','body')

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

        
