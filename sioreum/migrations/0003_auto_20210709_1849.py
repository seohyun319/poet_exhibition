# Generated by Django 3.2.3 on 2021-07-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sioreum', '0002_alter_visitform_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='backgroundImg',
            field=models.ImageField(blank=True, null=True, upload_to='sioreum/img/Images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='sioreum/img/thumbnailImages/'),
        ),
    ]