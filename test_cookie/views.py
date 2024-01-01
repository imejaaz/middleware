from django.shortcuts import render
from django.http import HttpResponse


def set_test_cookie(request):

    request.session.set_test_cookie()
    response = render(request, 'testc/set.html')
    return response

def check_test_cookie(request):

    statu = request.session.test_cookie_worked()
    print(statu)

    response = render(request, 'testc/get.html')
    return response

def delete_test_cookies(request):

    request.session.delete_test_cookie()
    return render(request, 'testc/del.html')

