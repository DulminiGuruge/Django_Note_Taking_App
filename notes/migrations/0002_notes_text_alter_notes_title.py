# Generated by Django 4.2.4 on 2023-09-01 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='text',
            field=models.TextField(default='s'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
