from django.contrib import admin


from .models import User, Member, Guide

admin.site.register(User)
admin.site.register(Member)
admin.site.register(Guide)