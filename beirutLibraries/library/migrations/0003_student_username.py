# Generated by Django 3.2.9 on 2021-11-30 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20211130_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='user', max_length=100),
            preserve_default=False,
        ),
    ]