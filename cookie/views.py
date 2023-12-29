from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  home(request):
    return HttpResponse("this is home page")

def set(request):

    obj = render(request, 'cookie/set.html')
    obj.set_signed_cookie('name', 'akhtar shayan', salt ='ejaz')
    return obj


# def get(request):
#     pass
# def del(request):
#     pass


