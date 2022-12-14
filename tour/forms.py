from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import Tour, Review, BookTour
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Div, Layout
from crispy_forms.layout import Submit

PROVINCE_CHOICES = [
    ('Amnat Charoen', 'Amnat Charoen'),
    ('Ang Thong', 'Ang Thong'),
    ('Ayutthaya', 'Ayutthaya'),
    ('Bangkok', 'Bangkok'),
    ('Buengkan', 'Buengkan'),
    ('Buri Ram', 'Buri Ram'),
    ('Chachoengsao', 'Chachoengsao'),
    ('Chai Nat', 'Chai Nat'),
    ('Chaiyaphum', 'Chaiyaphum'),
    ('Chanthaburi', 'Chanthaburi'),
    ('Chiang Mai', 'Chiang Mai'),
    ('Chiang Rai', 'Chiang Rai'),
    ('Chon Buri', 'Chon Buri'),
    ('Chumphon', 'Chumphon'),
    ('Kalasin', 'Kalasin'),
    ('Kamphaeng Phet', 'Kamphaeng Phet'),
    ('Kanchanaburi', 'Kanchanaburi'),
    ('Khonkaen', 'Khonkaen'),
    ('Krabi', 'Krabi'),
    ('Lampang', 'Lampang'),
    ('Lamphun', 'Lamphun'),
    ('Loburi', 'Loburi'),
    ('Loei', 'Loei'),
    ('Mae Hong Son', 'Mae Hong Son'),
    ('Maha Sarakham', 'Maha Sarakham'),
    ('Mukdahan', 'Mukdahan'),
    ('Nakhon Nayok', 'Nakhon Nayok'),
    ('Nakhon Pathom', 'Nakhon Pathom'),
    ('Nakhon Phanom', 'Nakhon Phanom'),
    ('Nakhon Ratchasima', 'Nakhon Ratchasima'),
    ('Nakhon Sawan', 'Nakhon Sawan'),
    ('Nakhon Si Thammarat', 'Nakhon Si Thammarat'),
    ('Nan', 'Nan'),
    ('Narathiwat', 'Narathiwat'),
    ('Nongbualamphu', 'Nongbualamphu'),
    ('Nong Khai', 'Nong Khai'),
    ('Nonthaburi', 'Nonthaburi'),
    ('Pathum Thani', 'Pathum Thani'),
    ('Pattani', 'Pattani'),
    ('Phangnga', 'Phangnga'),
    ('Phatthalung', 'Phatthalung'),
    ('Phayao', 'Phayao'),
    ('Phetchabun', 'Phetchabun'),
    ('Phetchaburi', 'Phetchaburi'),
    ('Phichit', 'Phichit'),
    ('Phitsanulok', 'Phitsanulok'),
    ('Phrae', 'Phrae'),
    ('Phuket', 'Phuket'),
    ('Prachin Buri', 'Prachin Buri'),
    ('Prachuap Khirikan', 'Prachuap Khirikan'),
    ('Ranong', 'Ranong'),
    ('Ratchaburi', 'Ratchaburi'),
    ('Rayong', 'Rayong'),
    ('Roi Et', 'Roi Et'),
    ('Sa Kaeo', 'Sa Kaeo'),
    ('Sakon Nakhon', 'Sakon Nakhon'),
    ('Samut Prakan', 'Samut Prakan'),
    ('Samut Sakhon', 'Samut Sakhon'),
    ('Samut Songkhram', 'Samut Songkhram'),
    ('Saraburi', 'Saraburi'),
    ('Satun', 'Satun'),
    ('Sing Buri', 'Sing Buri'),
    ('Sisaket', 'Sisaket'),
    ('Songkhla', 'Songkhla'),
    ('Sukhothai', 'Sukhothai'),
    ('Suphan Buri', 'Suphan Buri'),
    ('Surat Thani', 'Surat Thani'),
    ('Surin', 'Surin'),
    ('Tak', 'Tak'),
    ('Trang', 'Trang'),
    ('Trat', 'Trat'),
    ('Ubon Ratchathani', 'Ubon Ratchathani'),
    ('Udon Thani', 'Udon Thani'),
    ('Uthai Thani', 'Uthai Thani'),
    ('Uttaradit', 'Uttaradit'),
    ('Yala', 'Yala'),
    ('Yasothon', 'Yasothon'),
]

class TourForm(ModelForm):
    class Meta:
        model = Tour
        fields = ['t_name', 'province', 'price', 'amount', 'period', 'img', 'snippet', 'information',]

        widgets = {
            't_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'province' : forms.Select(choices=PROVINCE_CHOICES, attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'amount' : forms.NumberInput(attrs={'class': 'form-control'}),
            'period' : forms.TextInput(attrs={'class': 'form-control'}),
            'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
            'information' : forms.Textarea(attrs={'class': 'form-control'}),
        }                             


