from django.shortcuts import render, redirect

from data_collector.models import Measurement

def index(request):
    measurements = Measurement.objects.all()
    context = {
        "text": "List of measurements:",
        "measurements": measurements,
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == 'GET':
        return render(request, "create.html")
    elif request.method == 'POST':
        value = request.POST["value"]
        Measurement(value=value).save()
        return redirect("/")

