import json
import random

import geopy.distance
from django.core import serializers
from django.http import JsonResponse

from dk.models import Shop, Product, User


def init(request):
    items = list(User.objects.all())
    random_item = random.choice(items)
    return JsonResponse({'user_id': random_item.id})


def is_shop_available(shop, lat, long):
    return shop.is_open and shop.has_available_products and geopy.distance.distance((shop.latitude, shop.longitude),
                                                                                    (lat, long)) <= shop.service_radius


def shops(request, user_id, lat, long):
    lat = float(lat)
    long = float(long)
    ans = []
    for shop in Shop.objects.all():
        if is_shop_available(shop, lat, long):
            ans += [shop]
    return JsonResponse({'shops': json.loads(serializers.serialize('json', ans))})


def products(request, user_id, lat, long):
    lat = float(lat)
    long = float(long)
    ans = []
    for product in Product.objects.all():
        if is_shop_available(product.shop_id, lat, long):
            ans += [product]
    return JsonResponse({'products': json.loads(serializers.serialize('json', ans))})
