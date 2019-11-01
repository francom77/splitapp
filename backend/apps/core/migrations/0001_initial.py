# Generated by Django 2.1.4 on 2019-11-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('_deleted', models.BooleanField(default=False, editable=False)),
                ('reason', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')),
                ('state', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
