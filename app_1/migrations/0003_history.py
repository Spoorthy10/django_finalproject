# Generated by Django 3.2.5 on 2021-07-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0002_auto_20210719_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bookname', models.CharField(max_length=30)),
                ('Author', models.CharField(max_length=30)),
                ('Price', models.FloatField()),
                ('Summary', models.CharField(max_length=700)),
                ('Book', models.ImageField(upload_to='app_1/%y/%m/%d')),
            ],
        ),
    ]