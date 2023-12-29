from django.shortcuts import render
from datetime import timedelta, datetime
def set(request):

    res = render(request, 'verse/set.html')
    # res.set_cookie('name' , 'ijaz', expires=datetime.utcnow()+timedelta(days=1))
    res.set_cookie('name' , 'ijaz', max_age=30)
    return res

def get(request):

    # name = request.COOKIES['name']
    name = request.COOKIES.get('name', 'guest')


    res = render(request, 'verse/get.html', {'name': name})
  
    return res

def delete(request):
    res = render(request, 'verse/del.html')
    res.delete_cookie('name')
    return res