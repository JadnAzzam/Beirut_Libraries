# Generated by Django 3.2.9 on 2021-12-01 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='username',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
    ]
