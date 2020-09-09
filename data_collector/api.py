from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from data_collector.models import Measurement

@csrf_exempt
def list_all(request):
    measurements = Measurement.objects.all()

    measurements_dict = { str(m.pk): {
            "created": str(m.created),
            "value": m.value,
        } for m in measurements
    }

    data = {
        "text": "Hello world!",
        "total_items": measurements.count(),
        "measurements": measurements_dict,
    }
    return JsonResponse(data)

@csrf_exempt
def create(request):
    if request.method == 'GET':
        return JsonResponse({"status": "Fail"})
    elif request.method == 'POST':
        if "value" in request.POST:
            value = request.POST["value"]
            Measurement(value=value).save()
            status = "Ok"
        else:
            status = "Fail"
        return JsonResponse({"status": status})