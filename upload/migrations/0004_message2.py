# Generated by Django 2.0.5 on 2018-08-01 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0003_auto_20180705_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message2',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('note_id', models.IntegerField(blank=True, null=True)),
                ('message', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
