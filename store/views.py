from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from store.models import Store
from store.query.patchQuery import patchQuery
from store.query.postQuery import postQuery
from store.query.getQuery import getQuery
from store.query.putQuery import putQuery


def index(req):
    return HttpResponse("/items")
# Create your views here.
@csrf_exempt
def store(request):
    if request.method == "POST":
        return postQuery(dict(request.GET))
    elif request.method == "GET":
        return getQuery(dict(request.GET))
    elif request.method == "PUT":
        return putQuery(dict(request.GET))
    elif request.method == "PATCH":
        return patchQuery(dict(request.GET))
# def store(requests):
#     res=set()
#     data = Store.objects.all()
#     serilize = serializers.serialize('python',data)
#     return JsonResponse(serilize,safe=False)
    