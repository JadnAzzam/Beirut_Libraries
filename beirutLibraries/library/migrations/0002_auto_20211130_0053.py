# Generated by Django 3.2.9 on 2021-11-29 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(max_length=8)),
                ('librarian', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
