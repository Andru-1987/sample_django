# Generated by Django 4.1.3 on 2022-12-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_textcomment_editorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcomment',
            name='image_view',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]