# Generated by Django 4.1 on 2022-09-14 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]