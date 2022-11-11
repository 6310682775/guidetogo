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
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]
    PROVINCE = [

        ('Bankok', 'Bankok'),
        ('Samut Prakan', 'Samut Prakan'),
        ('Nonthaburi', 'Nonthaburi'),
        ('Pathum Thani', 'Pathum Thani'),
        ('Ayutthaya', 'Ayutthaya'),
        ('Ang Thong', 'Ang Thong'),
        ('Loburi', 'Loburi'),
        ('Sing Buri', 'Sing Buri'),
        ('Chai Nat', 'Chai Nat'),
        ('Saraburi', 'Saraburi'),
        ('Chon Buri', 'Chon Buri'),
        ('Rayong', 'Rayong'),
        ('Chanthaburi', 'Chanthaburi'),
        ('Trat', 'Trat'),
        ('Chachoengsao', 'Chachoengsao'),
        ('Prachin Buri', 'Prachin Buri'),
        ('Nakhon Nayok', 'Nakhon Nayok'),
        ('Sa Kaeo', 'Sa Kaeo'),
        ('Nakhon Ratchasima', 'Nakhon Ratchasima'),
        ('Buri Ram', 'Buri Ram'),
        ('Surin', 'Surin'),
        ('Sisaket', 'Sisaket'),
        ('Ubon Ratchathani', 'Ubon Ratchathani'),
        ('Yasothon', 'Yasothon'),
        ('Chaiyaphum', 'Chaiyaphum'),
        ('Amnat Charoen', 'Amnat Charoen'),
        ('Nongbualamphu', 'Nongbualamphu'),
        ('Khonkaen', 'Khonkaen'),
        ('Udon Thani', 'Udon Thani'),
        ('Loei', 'Loei'),
        ('Nonk Khai', 'Nonk Khai'),
        ('Maha Sarakham', 'Maha Sarakham'),
        ('Roi Et', 'Roi Et'),
        ('Kalasin', 'Kalasin'),
        ('Sakon Nakhon', 'Sakon Nakhon'),
        ('Nakhon Phanom', 'Nakhon Phanom'),
        ('Mukdahan', 'Mukdahan'),
        ('Chiang Mai', 'Chiang Mai'),
        ('Lamphun', 'Lamphun'),
        ('Lampang', 'Lampang'),
        ('Uttaradit', 'Uttaradit'),
        ('Phrae', 'Phrae'),
        ('Nan', 'Nan'),
        ('Phayao', 'Phayao'),
        ('Chiang Rai', 'Chiang Rai'),
        ('Mae Hong Son', 'Mae Hong Son'),
        ('Nakhon Sawan', 'Nakhon Sawan'),
        ('Uthai Thani', 'Uthai Thani'),
        ('Kamphaeng Phet', 'Kamphaeng Phet'),
        ('Tak', 'Tak'),
        ('Sukhothai', 'Sukhothai'),
        ('Phitsanulok', 'Phitsanulok'),
        ('Phichit', 'Phichit'),
        ('Phetchabun', 'Phetchabun'),
        ('Ratchaburi', 'Ratchaburi'),
        ('Kanchanaburi', 'Kanchanaburi'),
        ('Suphan Buri', 'Suphan Buri'),
        ('Nakhon Pathom', 'Nakhon Pathom'),
        ('Samut Sakhon', 'Samut Sakhon'),
        ('Samut Songkhram', 'Samut Songkhram'),
        ('Phetchaburi', 'Phetchaburi'),
        ('Prachuap Khirikan', 'Prachuap Khirikan'),
        ('Nakhon Si Thammarat', 'Nakhon Si Thammarat'),
        ('Krabi', 'Krabi'),
        ('Phangnga', 'Phangnga'),
        ('Phuket', 'Phuket'),
        ('Surat Thani', 'Surat Thani'),
        ('Ranong', 'Ranong'),
        ('Chumphon', 'Chumphon'),
        ('Songkhla', 'Songkhla'),
        ('Satun', 'Satun'),
        ('Trang', 'Trang'),
        ('Phatthalung', 'Phatthalung'),
        ('Pattani', 'Pattani'),
        ('Yala', 'Yala'),
        ('Narathiwat', 'Narathiwat'),
        ('Buengkan', 'Buengkan')

    ]
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

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]

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
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]
    PROVINCE = [

        ('Bankok', 'Bankok'),
        ('Samut Prakan', 'Samut Prakan'),
        ('Nonthaburi', 'Nonthaburi'),
        ('Pathum Thani', 'Pathum Thani'),
        ('Ayutthaya', 'Ayutthaya'),
        ('Ang Thong', 'Ang Thong'),
        ('Loburi', 'Loburi'),
        ('Sing Buri', 'Sing Buri'),
        ('Chai Nat', 'Chai Nat'),
        ('Saraburi', 'Saraburi'),
        ('Chon Buri', 'Chon Buri'),
        ('Rayong', 'Rayong'),
        ('Chanthaburi', 'Chanthaburi'),
        ('Trat', 'Trat'),
        ('Chachoengsao', 'Chachoengsao'),
        ('Prachin Buri', 'Prachin Buri'),
        ('Nakhon Nayok', 'Nakhon Nayok'),
        ('Sa Kaeo', 'Sa Kaeo'),
        ('Nakhon Ratchasima', 'Nakhon Ratchasima'),
        ('Buri Ram', 'Buri Ram'),
        ('Surin', 'Surin'),
        ('Sisaket', 'Sisaket'),
        ('Ubon Ratchathani', 'Ubon Ratchathani'),
        ('Yasothon', 'Yasothon'),
        ('Chaiyaphum', 'Chaiyaphum'),
        ('Amnat Charoen', 'Amnat Charoen'),
        ('Nongbualamphu', 'Nongbualamphu'),
        ('Khonkaen', 'Khonkaen'),
        ('Udon Thani', 'Udon Thani'),
        ('Loei', 'Loei'),
        ('Nonk Khai', 'Nonk Khai'),
        ('Maha Sarakham', 'Maha Sarakham'),
        ('Roi Et', 'Roi Et'),
        ('Kalasin', 'Kalasin'),
        ('Sakon Nakhon', 'Sakon Nakhon'),
        ('Nakhon Phanom', 'Nakhon Phanom'),
        ('Mukdahan', 'Mukdahan'),
        ('Chiang Mai', 'Chiang Mai'),
        ('Lamphun', 'Lamphun'),
        ('Lampang', 'Lampang'),
        ('Uttaradit', 'Uttaradit'),
        ('Phrae', 'Phrae'),
        ('Nan', 'Nan'),
        ('Phayao', 'Phayao'),
        ('Chiang Rai', 'Chiang Rai'),
        ('Mae Hong Son', 'Mae Hong Son'),
        ('Nakhon Sawan', 'Nakhon Sawan'),
        ('Uthai Thani', 'Uthai Thani'),
        ('Kamphaeng Phet', 'Kamphaeng Phet'),
        ('Tak', 'Tak'),
        ('Sukhothai', 'Sukhothai'),
        ('Phitsanulok', 'Phitsanulok'),
        ('Phichit', 'Phichit'),
        ('Phetchabun', 'Phetchabun'),
        ('Ratchaburi', 'Ratchaburi'),
        ('Kanchanaburi', 'Kanchanaburi'),
        ('Suphan Buri', 'Suphan Buri'),
        ('Nakhon Pathom', 'Nakhon Pathom'),
        ('Samut Sakhon', 'Samut Sakhon'),
        ('Samut Songkhram', 'Samut Songkhram'),
        ('Phetchaburi', 'Phetchaburi'),
        ('Prachuap Khirikan', 'Prachuap Khirikan'),
        ('Nakhon Si Thammarat', 'Nakhon Si Thammarat'),
        ('Krabi', 'Krabi'),
        ('Phangnga', 'Phangnga'),
        ('Phuket', 'Phuket'),
        ('Surat Thani', 'Surat Thani'),
        ('Ranong', 'Ranong'),
        ('Chumphon', 'Chumphon'),
        ('Songkhla', 'Songkhla'),
        ('Satun', 'Satun'),
        ('Trang', 'Trang'),
        ('Phatthalung', 'Phatthalung'),
        ('Pattani', 'Pattani'),
        ('Yala', 'Yala'),
        ('Narathiwat', 'Narathiwat'),
        ('Buengkan', 'Buengkan')

    ]
    email = forms.EmailField()
    age = forms.CharField()
    phone_number = forms.CharField()
    detail = forms.CharField()
    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'age',
                  'phone_number', 'detail']
