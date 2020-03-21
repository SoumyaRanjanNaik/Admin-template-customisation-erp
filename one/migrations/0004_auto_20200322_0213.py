# Generated by Django 3.0.2 on 2020-03-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_auto_20200321_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(blank=True, choices=[('Assigned', 'Assigned'), ('Requested', 'Requested'), ('Cancelled', 'Cancelled'), ('Rejected', 'Rejected'), ('Completed', 'Completed')], default='Requested', max_length=10, null=True),
        ),
    ]
