from django.shortcuts import render
from .models import Person
import requests


# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people':people})

#def index(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')
