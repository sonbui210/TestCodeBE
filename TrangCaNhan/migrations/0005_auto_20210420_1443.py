# Generated by Django 3.1.7 on 2021-04-20 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrangCaNhan', '0004_auto_20210420_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bantin',
            name='TenNguoiPost',
            field=models.CharField(default=' ', max_length=80, null=True),
        ),
    ]
