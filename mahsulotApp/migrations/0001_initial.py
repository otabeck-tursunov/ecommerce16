# Generated by Django 5.0.6 on 2024-05-20 11:14

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Katalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sarlavha', models.CharField(max_length=255, unique=True)),
                ('rasm', models.ImageField(upload_to='kataloglar/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=255)),
                ('batafsil', models.TextField(blank=True, null=True)),
                ('brend', models.CharField(blank=True, max_length=255)),
                ('dokon', models.CharField(blank=True, max_length=255)),
                ('narx', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('chegirma', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('miqdor', models.PositiveIntegerField(default=1)),
                ('kafolat', models.CharField(blank=True, max_length=255, null=True)),
                ('baho', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rasm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rasm', models.ImageField(upload_to='mahsulotlar/')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahsulotApp.mahsulot')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubKatalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sarlavha', models.CharField(max_length=255)),
                ('rasm', models.ImageField(upload_to='sub-kataloglar/')),
                ('katalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahsulotApp.katalog')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mahsulot',
            name='subKatalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahsulotApp.subkatalog'),
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('baho', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('izoh', models.TextField(blank=True, null=True)),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahsulotApp.mahsulot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('mahsulot', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Xususiyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nom', models.CharField(max_length=255)),
                ('qiymat', models.CharField(max_length=255)),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahsulotApp.mahsulot')),
            ],
            options={
                'unique_together': {('qiymat', 'nom')},
            },
        ),
    ]
