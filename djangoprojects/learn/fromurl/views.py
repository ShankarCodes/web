from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request,name,age,address):
    context={'name':name,'age':age,'address':address}
    return render(request,"fromurl\index.html",context)

