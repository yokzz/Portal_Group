# Generated by Django 5.0.6 on 2024-07-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_file', '0007_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='images/default/default_profile_picture.jpeg', null=True, upload_to='images/profile_photo'),
        ),
    ]