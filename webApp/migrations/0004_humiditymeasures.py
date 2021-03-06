# Generated by Django 2.2.6 on 2019-11-03 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_auto_20191102_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='HumidityMeasures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('device', models.CharField(max_length=255)),
                ('measure', models.DecimalField(decimal_places=3, max_digits=7)),
                ('message', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='webApp.Messages')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
