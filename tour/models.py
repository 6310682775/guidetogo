from django.db import models
from users.models import User, Guide, Member
from django.urls import reverse_lazy, reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Guide User
    reviewto = models.ForeignKey('tour.Tour', on_delete=models.CASCADE, related_name='reviewto')
    rating = models.IntegerField()
    content = models.TextField()
    date = models.DateTimeField()
    report = models.IntegerField(default=0)

    def __str__(self):
        return f'Reviewed {self.reviewto.t_name}: {self.rating} rating by {self.author}'

    class Meta:
        ordering = ['date']

class Tour(models.Model):
    t_name = models.CharField(max_length=200)
    guide = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tour_owner", blank=True) # owner (Guide User)
    province = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    period = models.CharField(max_length=50)
    amount = models.PositiveIntegerField(default=1)
    information = RichTextField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True,upload_to="images/tour/")
    review = models.ManyToManyField(Review, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.t_name}'

    def get_absolute_url(self):
        return reverse('tour:my_tour')
    class Meta:
        ordering = ['-date']
