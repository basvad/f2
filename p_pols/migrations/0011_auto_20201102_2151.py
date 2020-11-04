# Generated by Django 2.2.6 on 2020-11-02 18:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('p_pols', '0010_auto_20201102_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p_pols.Choice'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='p_pols.Poll'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='p_pols.Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='p_pols.UserProfile'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 2, 18, 51, 51, 315918, tzinfo=utc), help_text='Дата публикации', verbose_name='Дата публикации'),
        ),
    ]
