# Generated by Django 2.1.3 on 2018-11-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='_id',
            field=models.CharField(default=0, max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]