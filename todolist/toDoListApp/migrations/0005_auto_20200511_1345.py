# Generated by Django 3.0.6 on 2020-05-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoListApp', '0004_auto_20200511_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='priority',
            field=models.CharField(choices=[('low', 'low'), ('moderate', 'moderate'), ('high', 'high')], max_length=10, null=True),
        ),
    ]
