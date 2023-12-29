from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse

def home(request):
    IP =request.META.get('REMOTE_ADDR')
    print("your IP is: ", IP)
    print('view is here')

    return HttpResponse(IP)







def ex(request):
    print("this i ex view")
    a = 100/0

    # return HttpResponse("This is exception returned")
    
def user(request):
    print("you are in user view")
    context = {
        'name': 'ijaz ahmad'
    }
    return TemplateResponse(request, 'ind.html', context)