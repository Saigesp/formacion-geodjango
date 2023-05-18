from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry
from .models import Country
from django.http import JsonResponse


def generate_polygon_from_bbox(bbox):
    return GEOSGeometry(f"POLYGON(({bbox[0]} {bbox[1]},{bbox[0]} {bbox[3]},{bbox[2]} {bbox[3]},{bbox[2]} {bbox[1]},{bbox[0]} {bbox[1]}))")


def map(request):
    data = {
        "title": "Hola que tal",
    }
    return render(request, "countries.html", data)


def map_data(request):
    bbox = request.GET.get("bbox").split(',')
    container = generate_polygon_from_bbox(bbox)
    countries_in_bbox = Country.objects.filter(geometry__intersects=container)
    data = [{
        "name": country.name,
        "geometry": GEOSGeometry(country.geometry).geojson,
    } for country in countries_in_bbox]
    return JsonResponse({ "data": data })