from django.contrib.gis import admin
from countries.models import Country


# admin.ModelAdmin utiliza openlayers
# admin.GeoModelAdmin utiliza OpenStreetMap (poco zoom)
# admin.OSMGeoAdmin utiliza OpenStreetMap (maz zoom)

class CountryAdmin(admin.OSMGeoAdmin):
    pass


admin.site.register(Country, CountryAdmin)
