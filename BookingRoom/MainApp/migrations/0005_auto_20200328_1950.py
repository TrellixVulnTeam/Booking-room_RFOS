# Generated by Django 2.1.4 on 2020-03-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20200328_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomprofile',
            name='img_path',
            field=models.ImageField(upload_to='pict'),
        ),
    ]
