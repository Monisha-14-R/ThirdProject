from django.http import HttpResponse, request
from django.shortcuts import render


# Create your views here.
def index_fun(request):
    return render(request, 'index.html')


def readdata_fun(request):
    name = request.POST['txtName']  # to read textbox data
    age = request.POST['txtAge']
    email = request.POST['txtMail']
    return HttpResponse(f"Name= {name} Age= {age} Email= {email}")