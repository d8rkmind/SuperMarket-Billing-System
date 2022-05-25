from django.http import HttpResponse
from django.http.response import JsonResponse
from django.core import serializers
from store.models import Store

def index(req):
    return HttpResponse("/items")
# Create your views here.


def store(requests):
    res=set()
    data = Store.objects.all()
    serilize = serializers.serialize('json',data)
    return JsonResponse(serilize,safe=False)
    