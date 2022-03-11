from django.core import serializers
from django.http import JsonResponse

from dk.models import Shop, Product


def init(request):
    return JsonResponse({'user_id': 17})


def shops(request):
    return JsonResponse({'shops': serializers.serialize('json', Shop.objects.all())})


def products(request, user_id):
    return JsonResponse({'products': serializers.serialize('json', Product.objects.all())})
