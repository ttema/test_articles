# Generated by Django 3.0.3 on 2020-03-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20200316_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, upload_to='articles_images'),
        ),
    ]
