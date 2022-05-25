from django.http import HttpResponse
from .keyManage import postkeys
from store.models import Store
def postQuery(postdict:dict):
    if postkeys(postdict):
        instance = Store.objects.create(
            name=str(postdict["name"][0]),
            category=str(postdict['category'][0]),
            subcategory=str(postdict['subcategory'][0]),
            amount=int(postdict['amount'][0]))
        print(instance)

    return HttpResponse("Post")