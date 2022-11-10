from django.db import models
from users.models import User, Guide, Member

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
    information = models.TextField()
    img = models.ImageField(blank=True, null=True)
    review = models.ManyToManyField(Review, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.t_name}'

    class Meta:
        ordering = ['-date']
