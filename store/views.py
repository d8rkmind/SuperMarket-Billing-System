from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from store.models import Store
from store.query.postQuery import postQuery
from store.query.getQuery import getQuery


def index(req):
    return HttpResponse("/items")
# Create your views here.
@csrf_exempt
def store(request):
    if request.method == "POST":
        print(request.POST)
        return postQuery(dict(request.GET))
    elif request.method == "GET":
        return getQuery(dict(request.GET))
        

# def store(requests):
#     res=set()
#     data = Store.objects.all()
#     serilize = serializers.serialize('python',data)
#     return JsonResponse(serilize,safe=False)
    