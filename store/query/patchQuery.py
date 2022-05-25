from django.http import JsonResponse
from .keyManage import postkeys
from store.models import Store

def patchQuery(patchdict:dict):
    if postkeys(patchdict):
        if Store.objects.filter(name=str(patchdict['name'][0])).exists():
            t=Store.objects.get(name=str(patchdict['name'][0]))
            t.category=str(patchdict['category'][0])
            t.subcategory=str(patchdict['subcategory'][0])     
            t.amount=int(patchdict['amount'][0])
            t.save()
            return JsonResponse({"200":"Updated Existing object"},safe=False)
        return JsonResponse({"417":"Expectation Failed"},status=417)
    return JsonResponse({"404":"Expectation Failed"},status=404)