# Generated by Django 3.0.5 on 2020-04-21 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_app', '0003_delete_login_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('Job', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=128)),
            ],
        ),
    ]
