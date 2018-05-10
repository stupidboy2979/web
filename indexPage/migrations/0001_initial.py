# Generated by Django 2.0.2 on 2018-05-10 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trunk', models.IntegerField()),
                ('port', models.CharField(max_length=20)),
                ('sgNum', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.CharField(max_length=20)),
                ('portal', models.CharField(max_length=20)),
                ('das', models.IntegerField()),
                ('dpc', models.CharField(max_length=20)),
                ('creatDate', models.DateField()),
                ('circuits', models.ManyToManyField(to='indexPage.Circuit')),
            ],
        ),
    ]
