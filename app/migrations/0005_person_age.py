# Generated by Django 3.2.3 on 2021-07-09 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
