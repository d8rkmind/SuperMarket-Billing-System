from django.http import  JsonResponse
from .keyManage import getkeys
from store.models import Store
from django.core import serializers


def nodata():
    return JsonResponse({"404": "No Data Found"}, safe=False, status=404)


def all_data():
    serialize = serializers.serialize("python", Store.objects.all())
    return JsonResponse(serialize, safe=False)


def spec_data_by_name(value):
    if Store.objects.filter(name=str(value)).exists():
        return JsonResponse(serializers.serialize("python", Store.objects.filter(name=value)), safe=False)
    return nodata()


def spec_data_by_category(value):
    if Store.objects.filter(category=str(value)).exists():
        return JsonResponse(serializers.serialize("python", Store.objects.filter(category=value)), safe=False)
    return nodata()


def spec_data_by_subcategory(value):
    if Store.objects.filter(subcategory=str(value)).exists():
        return JsonResponse(serializers.serialize("python", Store.objects.filter(subcategory=value)), safe=False)
    return nodata()


def spec_data_by_amount(value):
    if Store.objects.filter(amount=str(value)).exists():
        return JsonResponse(serializers.serialize("python", Store.objects.filter(amount=str(value))), safe=False)
    return nodata()


def getQuery(getdict: dict):
    try:
        if not bool(getdict):
            return all_data()
        elif getkeys(getdict):
            val = list(getdict.keys())[0]
            paramater = getdict[val][0]
            if val == "name":
                return spec_data_by_name(paramater)
            elif val == "category":
                return spec_data_by_category(paramater)
            elif val == "subcategory":
                return spec_data_by_subcategory(paramater)
            elif val == "amount":
                return spec_data_by_amount(paramater)
            else:
                return JsonResponse({"400": "Bad Request"}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({"500":"Internal server Error"}, status=500)
