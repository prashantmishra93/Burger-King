# Generated by Django 3.1.4 on 2021-01-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dynamic_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=30)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]