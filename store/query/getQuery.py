from django.http import HttpResponse,JsonResponse
from .keyManage import keys
from store.models import Store
from django.core import serializers

def all_data():
    serialize = serializers.serialize('python',Store.objects.all())
    return JsonResponse(serialize,safe=False)

def spec_data_by_name(value):
    return JsonResponse(serializers.serialize("python",Store.objects.filter(name=value)),safe=False)

def spec_data_by_category(value):
    return JsonResponse(serializers.serialize("python",Store.objects.filter(category=value)),safe=False)

def spec_data_by_subcategory(value):
    return JsonResponse(serializers.serialize("python",Store.objects.filter(subcategory=value)),safe=False)

def spec_data_by_amount(value):
    return JsonResponse(serializers.serialize("python",Store.objects.filter(amount=value)),safe=False)

def getQuery(getdict:dict):
    try:
        if not bool(getdict):
            return all_data()
        elif keys(getdict):
            val=list(getdict.keys())[0]
            paramater = getdict[val][0]
            if val=="name":
                return spec_data_by_name(paramater)
            elif val=="category":
                return spec_data_by_category(paramater)
            elif val=="subcategory":
                return spec_data_by_subcategory(paramater)
            elif val=="amount":
                return spec_data_by_amount(paramater)
            else:
                return HttpResponse("Not found")
    except Exception as e:
                print(e)
                return HttpResponse("Internal server Error",status=500)
    finally:
        print("[+] Get Request Done")