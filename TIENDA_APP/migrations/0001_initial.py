# Generated by Django 3.2.6 on 2021-08-30 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mi_modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Apellido', models.CharField(max_length=30)),
                ('number_tarjeta', models.IntegerField(max_length=16)),
                ('fecha_tarjeta', models.DateField()),
                ('codigo_seguridad', models.IntegerField(max_length=3)),
            ],
        ),
    ]
