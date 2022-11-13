from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import Tour, Review
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Div, Layout
from crispy_forms.layout import Submit

PROVINCE_CHOICES = [
    ('Amnat Charoen', 'Amnat Charoen'), 
    ('Ang Thong', 'Ang Thong'),
    ('Ayutthaya', 'Ayutthaya'),
    ('Bangkok', 'Bangkok'),
    ('Bueng Kan', 'Bueng Kan'),
]

class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['t_name', 'province', 'price', 'amount', 'period', 'img', 'information',]

        widgets = {
            't_name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'this is placeholder'}),
            'province' : forms.Select(choices=PROVINCE_CHOICES,attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'amount' : forms.NumberInput(attrs={'class': 'form-control'}),
            'period' : forms.TextInput(attrs={'class': 'form-control'}),
            'information' : forms.Textarea(attrs={'class': 'form-control'}),
        
        }

class UpdateTourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['t_name', 'province', 'price', 'amount', 'period', 'img', 'information',]

        widgets = {
            't_name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'this is placeholder'}),
            'province' : forms.Select(choices=PROVINCE_CHOICES,attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'amount' : forms.NumberInput(attrs={'class': 'form-control'}),
            'period' : forms.TextInput(attrs={'class': 'form-control'}),
            'information' : forms.Textarea(attrs={'class': 'form-control'}),
        
        }

    # t_title = forms.CharField(label='Title', max_length=200)
    # province = forms.ChoiceField(label='Tour Area', choices=PROVINCE_CHOICES)
    # price = forms.IntegerField(label='Price per group (THB)',)
    # amount = forms.IntegerField(max_value=20, min_value=1)
    # period = forms.CharField()
    # img = forms.ImageField(label='Image', required=False)
    # information = forms.CharField(label='Detail', max_length=500, widget=forms.Textarea(), help_text='You can add locations by click the emoji below and type location name')
    # date_add = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'min': datetime.now().date(), 'max': datetime.now().date()}))                               
