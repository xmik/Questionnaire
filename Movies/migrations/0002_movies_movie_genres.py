# Generated by Django 2.2.6 on 2019-10-11 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_genres',
            field=models.CharField(default='', max_length=800),
            preserve_default=False,
        ),
    ]
