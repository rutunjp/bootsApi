# Generated by Django 4.2.1 on 2023-05-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_boot_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boot',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
