# Generated by Django 3.1.6 on 2021-03-01 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_auto_20210110_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HP', models.IntegerField(null=True)),
                ('IQ', models.IntegerField(null=True)),
                ('FUN', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='strhistory',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
