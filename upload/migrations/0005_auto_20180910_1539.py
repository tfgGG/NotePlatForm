# Generated by Django 2.0.7 on 2018-09-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0004_message2'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadMessage2',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('note_id', models.IntegerField(blank=True, null=True)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'upload_message2',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='message2',
            name='user',
        ),
        migrations.DeleteModel(
            name='Message2',
        ),
    ]
