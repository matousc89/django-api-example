from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from blog.models import Measurement

# Create your views here.

@csrf_exempt
def homepage(request):
    msg = ""
    if request.method == "GET":
        msg = "Please fill data."
    else:
        if "measurement" in request.POST:
            value = request.POST["measurement"]
            m = Measurement(
                value=value,
            )
            m.save()
            msg = "Value: {}, was saved".format(value)
        else:
            msg = "No data provided - no data saved."

    values = Measurement.objects.all()
    return render(request, "index.html", context={"msg": msg, "values": values})





