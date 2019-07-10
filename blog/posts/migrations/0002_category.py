# Generated by Django 2.1 on 2019-07-09 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.TimeStampedModel')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=10, unique=True)),
            ],
            bases=('posts.timestampedmodel',),
        ),
    ]