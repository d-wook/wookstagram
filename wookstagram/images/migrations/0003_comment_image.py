# Generated by Django 2.0.2 on 2018-03-10 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180310_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
    ]
