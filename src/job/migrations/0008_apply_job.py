# Generated by Django 3.1.4 on 2021-01-06 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='Job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='job.job'),
            preserve_default=False,
        ),
    ]
