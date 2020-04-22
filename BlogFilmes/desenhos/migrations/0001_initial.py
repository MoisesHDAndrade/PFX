# Generated by Django 3.0.4 on 2020-04-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desenhos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_desenho', models.CharField(max_length=50, verbose_name='Desenho')),
                ('url_desenho', models.TextField()),
                ('img_desenho', models.TextField()),
            ],
            options={
                'verbose_name': 'Desenho',
                'verbose_name_plural': 'Desenhos',
            },
        ),
    ]
