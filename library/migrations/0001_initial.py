# Generated by Django 2.2 on 2019-04-16 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('quantity', models.PositiveIntegerField(default=10, verbose_name='Quantity')),
                ('date_pub', models.PositiveSmallIntegerField(verbose_name='Date of publication')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.Author', verbose_name='Author')),
                ('categories', models.ManyToManyField(related_name='books', to='library.Category', verbose_name='Categories')),
                ('readers', models.ManyToManyField(blank=True, related_name='books', to=settings.AUTH_USER_MODEL, verbose_name='Readers')),
            ],
        ),
    ]