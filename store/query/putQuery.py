from django.http import JsonResponse
from .keyManage import postkeys
from store.models import Store


def putQuery(putdict: dict):
    if postkeys(putdict):
        if Store.objects.filter(name=str(putdict['name'][0])).exists():
            t = Store.objects.get(name=str(putdict['name'][0]))
            t.category = str(putdict['category'][0])
            t.subcategory = str(putdict['subcategory'][0])
            t.amount = int(putdict['amount'][0])
            t.save()
            return JsonResponse({"200": "Updated Existing object"}, safe=False)
        else:
            instance = Store.objects.create(
                name=str(putdict["name"][0]),
                category=str(putdict['category'][0]),
                subcategory=str(putdict['subcategory'][0]),
                amount=int(putdict['amount'][0]))
            return JsonResponse({"200": "Created New Object"}, safe=False)
    else:
        return JsonResponse({"400": "Bad request"}, safe=False, status=400)
