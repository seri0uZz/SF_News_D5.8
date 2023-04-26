# Generated by Django 4.2 on 2023-04-20 17:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='news.author'),
            preserve_default=False,
        ),
    ]