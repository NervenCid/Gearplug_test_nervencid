# Generated by Django 4.2.6 on 2023-10-14 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemonName', models.CharField(max_length=200)),
                ('abilities', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemonName', models.CharField(max_length=200)),
                ('order', models.IntegerField()),
                ('abilities', models.ManyToManyField(to='Poketasks.ability')),
            ],
        ),
    ]
