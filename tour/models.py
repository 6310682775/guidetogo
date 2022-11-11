from django.db import models
from users.models import User, Guide, Member
from datetime import datetime
from django.utils.timezone import now
# Create your models here.
'''
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Guide User
    reviewto = models.ForeignKey('tour.Tour', on_delete=models.CASCADE, related_name='reviewto')
    stars = models.IntegerField()
    content = models.TextField()
    date = models.DateTimeField()
    report = models.IntegerField(default=0)

    def __str__(self):
        return f'Reviewed {self.reviewto.t_name}: {self.reviewto} rating by {self.author}'

    class Meta:
        ordering = ['date']
'''
class Review(models.Model):
    reviewed_tour = models.ManyToManyField(User, blank=True, related_name='comtour')
    review_name = models.CharField(max_length=300, null=True, blank=True)
    review_text = models.CharField(max_length=300,null=True, blank=True)
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(default= datetime.now(),blank=True, null=True)

    def __str__(self):
        return  f"{self.reviewed_tour} : {self.review_name}  {self.review_text}"
    class Meta:
        ordering = ['date']

class Tour(models.Model):
    
    t_name = models.CharField(max_length=200)
    guide = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tour_owner", blank=True) # owner (Guide User)
    province = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    period = models.CharField(max_length=50)
    amount = models.PositiveIntegerField(default=1)
    information = models.TextField()
    img = models.ImageField(blank=True, null=True)
    review = models.ManyToManyField(Review, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.t_name}'

    class Meta:
        ordering = ['-date']
