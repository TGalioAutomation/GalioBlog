# Generated by Django 3.1.5 on 2021-05-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210517_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]