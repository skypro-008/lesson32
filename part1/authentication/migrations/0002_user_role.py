# Generated by Django 3.2.7 on 2022-01-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('unknown', 'unknown'), ('employee', 'employee'), ('hr', 'hr')], default='unknown', max_length=8),
        ),
    ]
