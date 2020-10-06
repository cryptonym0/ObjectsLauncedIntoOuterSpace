from django.db import models


# Simple Space Object
class SpaceObject(models.Model):
    name_of_space_object_ino_s1 = models.CharField(max_length=100)
    launch_state_of_registry = models.CharField(max_length=100)
    launch_date = models.DateTimeField('date launched')
    object_status = models.CharField(max_length=100)
    object_remarks = models.CharField(max_length=200)


# Launch Facilities
