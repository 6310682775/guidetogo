from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Member, Guide

PROVINCE = [
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

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
    ('I prefer not to say', 'I prefer not to say'),
]


class MemberSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    age = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    allergic = forms.CharField(required=True)
    underlying_disease = forms.CharField(required=True)
    religion = forms.CharField(required=True)
    member_image = forms.ImageField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_member = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        member = Member.objects.create(user=user)
        member.address = self.cleaned_data.get('address')
        member.phone_number = self.cleaned_data.get('phone_number')
        member.email = self.cleaned_data.get('email')
        member.age = self.cleaned_data.get('age')
        member.gender = self.cleaned_data.get('gender')
        member.allergic = self.cleaned_data.get('allergic')
        member.underlying_disease = self.cleaned_data.get('underlying_disease')
        member.religion = self.cleaned_data.get('religion')
        member.member_image = self.cleaned_data.get('member_image')
        member.save()
        return user


class GuideSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    age = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    detail = forms.CharField(required=True)
    province = forms.ChoiceField(choices=PROVINCE, required=True)
    tat_license = forms.CharField(required=True)
    guide_image = forms.ImageField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guide = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        guide = Guide.objects.create(user=user)
        guide.phone_number = self.cleaned_data.get('phone_number')
        guide.detail = self.cleaned_data.get('detail')
        guide.email = self.cleaned_data.get('email')
        guide.age = self.cleaned_data.get('age')
        guide.gender = self.cleaned_data.get('gender')
        guide.address = self.cleaned_data.get('address')
        guide.province = self.cleaned_data.get('province')
        guide.tat_license = self.cleaned_data.get('tat_license')
        guide.guide_image = self.cleaned_data.get('guide_image')
        guide.save()
        return user

class UpdateMemberForm(forms.ModelForm):
    age = forms.CharField()
    phone_number = forms.CharField()
    address = forms.CharField()
    allergic = forms.CharField()
    underlying_disease = forms.CharField()
    religion = forms.CharField()

    class Meta:
        model = User
        fields = ['age', 'phone_number',
                  'address', 'allergic', 'underlying_disease', 'religion']


class UpdateGuideForm(forms.ModelForm):
    email = forms.EmailField()
    age = forms.CharField()
    phone_number = forms.CharField()
    detail = forms.CharField()
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'age',
                  'phone_number', 'detail']
