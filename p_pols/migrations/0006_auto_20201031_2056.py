# Generated by Django 2.2.6 on 2020-10-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_pols', '0005_poll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='poll',
        ),
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ManyToManyField(to='p_pols.Poll'),
        ),
    ]