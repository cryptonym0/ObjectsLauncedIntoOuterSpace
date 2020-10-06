from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpaceObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_space_object_ino_s1', models.CharField(max_length=100)),
                ('lauch_state_of_registry', models.CharField(max_length=100)),
                ('launch_date', models.DateTimeField(verbose_name=b'date launched')),
                ('object_status', models.CharField(max_length=100)),
                ('object_remarks', models.CharField(max_length=200)),
            ],
        ),
    ]
