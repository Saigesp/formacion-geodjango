from django.contrib.gis.db import models


class Country(models.Model):
    name = models.CharField(
        max_length=255,
    )
    geometry = models.GeometryField(db_index=True)

    def __str__(self):
        return self.name
