from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
# def substract(request):
    # c=a-b


    # return HttpResponse( "hello")
    # return HttpResponse("Your answer is==>" + str(c))

def substract(request):
   my_data = request.GET
   a=float(my_data.get('a'))
   b=float(my_data.get('b'))
   c=a-b
   return HttpResponse("Your sum is==>" + str(c))

