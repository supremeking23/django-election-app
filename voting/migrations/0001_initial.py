# Generated by Django 2.2.9 on 2020-02-11 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(null=True)),
                ('image', models.ImageField(upload_to='image/')),
                ('count', models.IntegerField(null=True)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.Position')),
            ],
        ),
    ]
