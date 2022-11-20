# Generated by Django 4.1.1 on 2022-11-20 13:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookTour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verify_member', models.CharField(choices=[('verified', 'verified'), ('denied', 'denied'), ('not_verified', 'not_verified')], default='not_verified', max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=200)),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=200)),
                ('province', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('period', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('snippet', models.CharField(max_length=255)),
                ('information', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/tour/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('verify_tour', models.BooleanField(default=False)),
                ('avg_rating', models.IntegerField(blank=True, default=0, null=True)),
                ('book', models.ManyToManyField(blank=True, related_name='book_tour', to='tour.booktour')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
