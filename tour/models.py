from datetime import datetime
from django.db.models import Avg
from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from users.models import Guide, Member, User

# Create your models here.

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE,)
    review_tour = models.ManyToManyField('tour.Tour', blank=True, related_name='this_tour')
    review_title = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f'{self.review_tour} : {self.review_title}  {self.review_text}'
    class Meta:
        ordering = ['-date']


class BookTour(models.Model):
    verify_choices = (
        ('verified', 'verified'),
        ('denied', 'denied'),
        ('not_verified', 'not_verified'),
    )

    tour = models.ForeignKey( 'tour.Tour', on_delete=models.CASCADE,  related_name="book_tour",blank=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="book_member",blank=True)
    verify_member = models.CharField(max_length=15, choices=verify_choices, default='not_verified')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tour(models.Model):
    
    t_name = models.CharField(max_length=200)
    guide = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tour_owner", blank=True) # owner (Guide User)
    province = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    period = models.CharField(max_length=50)
    amount = models.PositiveIntegerField(default=1)
    snippet = models.CharField(max_length=255)
    information = RichTextField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True, upload_to="images/tour/")
    review = models.ManyToManyField(Review, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verify_tour = models.BooleanField(default=False)
    book = models.ManyToManyField( BookTour, blank=True,related_name='book_tour')
    avg_rating = models.IntegerField(null = True, default = 0,blank=True )
    

    def __str__(self):
        return f'{self.t_name}'

    def get_absolute_url(self):
        return reverse('tour:my_tour_guide')
    class Meta:
        ordering = ['-date']

