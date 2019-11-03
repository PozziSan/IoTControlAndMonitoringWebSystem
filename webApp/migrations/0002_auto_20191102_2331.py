# Generated by Django 2.2.6 on 2019-11-03 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('topic', models.CharField(max_length=255)),
                ('device', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(0, 'Received'), (1, 'Sent')], default=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='temperaturemeasures',
            name='device',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviceactivationlog',
            name='message',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='webApp.Messages'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temperaturemeasures',
            name='message',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='webApp.Messages'),
            preserve_default=False,
        ),
    ]
