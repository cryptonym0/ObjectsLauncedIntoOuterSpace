from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olios_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spaceobject',
            old_name='lauch_state_of_registry',
            new_name='launch_state_of_registry',
        ),
    ]
