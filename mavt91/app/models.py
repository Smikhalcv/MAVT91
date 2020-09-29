from django.db import models
from django.contrib.gis.db import models as gis_models


class Coordinates(models.Model):
    coordinates = gis_models.PointField()