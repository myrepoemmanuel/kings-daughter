# Generated by Django 4.1.6 on 2023-06-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='article_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
