# Generated by Django 4.0.4 on 2022-12-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
    ]
