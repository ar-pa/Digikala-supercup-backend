import json
import geopy.distance

from django.core import serializers
from django.http import JsonResponse

from dk.models import Shop, Product


def init(request):
    return JsonResponse({'user_id': 17})


def shops(request, user_id, lat, long):
    lat = float(lat)
    long = float(long)
    ans = []
    for shop in Shop.objects.all():
        if shop.is_open and shop.has_available_products and geopy.distance.distance((shop.latitude, shop.longitude),
                                                                                    (lat, long)) <= shop.service_radius:
            ans += [shop]
    return JsonResponse({'shops': json.loads(serializers.serialize('json', ans))})


def products(request, user_id):
    return JsonResponse({'products': serializers.serialize('json', Product.objects.all())})
