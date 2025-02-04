# Generated by Django 5.1.1 on 2024-10-03 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PorteFolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='folioapp/media/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='photo',
            field=models.ImageField(upload_to='folioapp/media/'),
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='folioapp/media/technologies/')),
                ('portefolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='folioapp.portefolio')),
            ],
        ),
    ]
