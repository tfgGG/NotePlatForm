# Generated by Django 2.1.3 on 2018-11-29 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_auto_20181010_0012'),
        ('person', '0005_myapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groupnote',
            fields=[
                ('idgroupnote', models.AutoField(primary_key=True, serialize=False)),
                ('group', models.ForeignKey(blank=True, db_column='group', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='person.Group')),
                ('note', models.ForeignKey(blank=True, db_column='note', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='upload.Note')),
            ],
        ),
    ]
