# Generated by Django 2.2.9 on 2020-02-11 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_auto_20200211_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='votes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]