# Generated by Django 3.1.7 on 2021-03-31 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0002_prime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prime1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prime_f', models.CharField(max_length=500)),
                ('prime_s', models.CharField(max_length=500)),
                ('times', models.CharField(max_length=500)),
                ('timelaps', models.CharField(max_length=500)),
                ('totalprime', models.CharField(max_length=500000000000000000000000)),
            ],
        ),
    ]
