# Generated by Django 4.1.3 on 2022-12-05 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textcomment',
            name='editorial',
            field=models.CharField(choices=[('PNG', 'Penguin'), ('ATL', 'Atlas'), ('ATH', 'Atheneo')], default='ATL', max_length=3),
        ),
    ]
