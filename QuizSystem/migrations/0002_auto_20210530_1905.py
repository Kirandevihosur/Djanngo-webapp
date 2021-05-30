# Generated by Django 3.2.3 on 2021-05-30 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuizSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('university', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
