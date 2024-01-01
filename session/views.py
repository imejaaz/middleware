from django.shortcuts import render




def set_test_cookie(request):
    test = request.session.set_test_cookie()
    print(test)
# Create your views here.
def setSession(request):

    request.session.set_expiry(90)
    request.session['name'] = 'ejaz ahmad'
    request.session['age'] = '24'
    obj = render(request, 'session/set.html')
    return obj


def getSession(request):

    # name = request.session.get('name', '')
    # age = request.session.get('age', '')
    # items = request.session.items()
    # keys = request.session.keys()
    # request.session.setdefault('age', 20)
    # return render(request, 'session/get.html', {'name' :name, 'age':age, 'keys': keys, 'items':items})

    name = request.session.get('name', '')
    # print(request.session.get_session_cookie_age)
    # print(request.session.get_expiry_date)
    # print(request.session.get_expiry_age)
    # print(request.session.get_expire_at_browser_close)

    return render(request, 'session/get.html', {'name' :name})

def deleteSession(request):

    # if 'name' in request.session:
    #     del request.session['name']

    request.session.clear_expired()
    request.session.flush()

    return render(request, 'session/del.html')