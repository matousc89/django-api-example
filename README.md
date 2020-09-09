# Django ukázka

1. vytvoření projektu
    > django-admin startproject mysite

1. testovací server
    > python manage.py runserver

1. migrace databáze
    > python manage.py migrate

1. vytvoření migrací databáze
    > python manage.py makemigrations

1. vytvoření super uživatele
    > python manage.py createsuperuser 

1. settings

1. django urls: https://docs.djangoproject.com/en/3.1/topics/http/urls/
   
1. views.py:
   
    ```
    from django.shortcuts import render
    
    def index(request):
        return render(request, "index.html")
    ```
1. models.py:
    ```
    from django.db import models
    
    class Measurement(models.Model):
    
    value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.value)
    ```

1. admin.py
   ```
   from django.contrib import admin
   from myproject.myapp.models import Author
    
   admin.site.register(Author)
   ```
   
1. api.py:
    ```
    from django.http import JsonResponse
   
    def list_all(request):
        data = {
            "text": "Hello world!"
        }
        return JsonResponse(data)
    ```
   
1. api.py (csrf exempt):
    ```
    from django.views.decorators.csrf import csrf_exempt
    ```

1. api.py:
    ```
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
    ```