# Generated by Django 5.0.1 on 2024-01-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, default='Team GreenClean', max_length=100, null=True),
        ),
    ]
