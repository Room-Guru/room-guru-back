# Generated by Django 3.2.4 on 2023-08-01 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_plan_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='plan_type',
            field=models.CharField(default=True, max_length=20, null=True),
        ),
    ]