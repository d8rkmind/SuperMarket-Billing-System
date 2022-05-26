from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from store.query.patchQuery import patchQuery
from store.query.postQuery import postQuery
from store.query.getQuery import getQuery
from store.query.putQuery import putQuery


def index(req):
    return JsonResponse({'404': 'Endpoint not found', 'avaliable_endpoint': '/items'}, status=404)
# Create your views here.


@csrf_exempt
def store(request):
    try:
        if request.method == "POST":
            return postQuery(dict(request.GET))
        elif request.method == "GET":
            return getQuery(dict(request.GET))
        elif request.method == "PUT":
            return putQuery(dict(request.GET))
        elif request.method == "PATCH":
            return patchQuery(dict(request.GET))
        else:
            return JsonResponse({'405': 'Method Not allowed'}, status=405)
    except:
        return JsonResponse({'500': 'internal server error'}, status=500)
