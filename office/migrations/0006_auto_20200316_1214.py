# Generated by Django 3.0.3 on 2020-03-16 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_auto_20200316_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, default=None, height_field=100, upload_to='articles_images', width_field=100),
        ),
    ]