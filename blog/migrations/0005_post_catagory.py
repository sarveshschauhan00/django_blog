# Generated by Django 4.0.2 on 2022-06-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_catagory'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catagory',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
