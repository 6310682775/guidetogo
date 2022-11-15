from django.contrib import admin
from .models import Tour, Review, BookTour

# Register your models here.

admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(BookTour)