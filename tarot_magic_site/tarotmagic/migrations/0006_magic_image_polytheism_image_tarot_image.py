# Generated by Django 4.2.8 on 2024-01-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarotmagic', '0005_alter_magic_options_alter_polytheism_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='magic',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='polytheism',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='tarot',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos', verbose_name='Image'),
        ),
    ]