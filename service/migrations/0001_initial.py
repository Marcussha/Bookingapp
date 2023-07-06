# Generated by Django 4.2.3 on 2023-07-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('serviceid', models.IntegerField(db_column='ServiceID', primary_key=True, serialize=False)),
                ('name_service', models.CharField(db_column='Name_service', max_length=50)),
            ],
            options={
                'db_table': 'services',
                'managed': False,
            },
        ),
    ]