# Generated by Django 2.2.7 on 2020-08-04 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pos',
            field=models.CharField(default='', max_length=20000),
            preserve_default=False,
        ),
    ]
