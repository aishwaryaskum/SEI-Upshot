# Generated by Django 2.1.11 on 2020-04-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resultApp', '0005_auto_20200427_1730'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carryover',
            unique_together={('roll', 'year_of_result', 'semester')},
        ),
    ]
