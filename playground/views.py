from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


# Create your views here.


# def say_hello(request):
#     return HttpResponse("Hello world")

def say_hello(request):
    try:
        query_set = Product.objects.filter(unit_price__gt=20).first()
    except:
        pass
          
    for prod in query_set:
     print("prod : ",prod)
    return render(request, 'hello.html', {'name': 'PKS'},{'product': list(query_set)})
    