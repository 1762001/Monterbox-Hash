# Generated by Django 2.2.2 on 2019-12-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_page', '0006_auto_20191208_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_name',
            field=models.CharField(max_length=100),
        ),
    ]