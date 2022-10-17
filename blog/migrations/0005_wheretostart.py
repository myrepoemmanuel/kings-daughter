# Generated by Django 3.2.5 on 2022-10-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20221008_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhereToStart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='welcome')),
                ('title', models.TextField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Where  To  Start',
            },
        ),
    ]