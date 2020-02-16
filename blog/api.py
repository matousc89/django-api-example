from django.http import JsonResponse

from blog.models import Measurement

def values(request):
    # params
    number = int(request.GET["number"])

    # query
    selection = Measurement.objects.all().order_by("-created")
    number = number if number < selection.count() else selection.count()
    selection = selection[:number]

    # serialization
    data = {"values": [
        {
            "value": m.value,
            "id": m.pk,
            "created": m.created,
        } for m in selection
    ]}

    return JsonResponse(data)

def create(request):
    if "value" in request.GET:
        value = request.GET["value"]
        try:
            value = int(value)
            try:
                Measurement(value=value).save()
                status = "Ok."
            except:
                status = "Unable to create new record."
        except:
            status = "Unable to understand the value."
    else:
        status = "Missing value."
    data = {
        "status": status
    }
    return JsonResponse(data)

def delete(request):
    if "id" in request.GET:
        pk = int(request.GET["id"])
        try:
            Measurement.objects.get(pk=pk).delete()
            status = "Object deleted."
        except:
            status = "Object was not deleted"
    else:
        status = "Missing id (pk)."
    data = {
        "status": status
    }
    return JsonResponse(data)
