from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
		my_d={'insert':"kya bey kya bolta hai"}
		return render(request,"index.html",context=my_d)
		# ~ return HttpResponse("<h1>Hello Rajesh How are You</h1>")

'''


{% load staticfiles %}

<img src="{% static "image/jj.png"%}"> 

'''
