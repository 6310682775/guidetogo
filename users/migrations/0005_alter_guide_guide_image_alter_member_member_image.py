# Generated by Django 4.1.3 on 2022-11-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_guide_guide_image_alter_member_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='guide_image',
            field=models.ImageField(blank=True, upload_to='main/storeimg'),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(blank=True, upload_to='main/storeimg'),
        ),
    ]
