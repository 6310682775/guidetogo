from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Member, Guide


class MemberSignUpForm(UserCreationForm):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]
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
    member_image = forms.ImageField()

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
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    age = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
    address = forms.CharField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    detail = forms.CharField(required=True)
    province = forms.CharField(required=True)
    tat_license = forms.CharField(required=True)
    guide_image = forms.ImageField()

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
