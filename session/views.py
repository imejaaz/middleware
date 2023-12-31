from django.shortcuts import render


# Create your views here.
def setSession(request):

    request.session['name'] = 'ejaz ahmad'
    obj = render(request, 'session/set.html')
    return obj


def getSession(request):

    name = request.session.get('name', '')
    return render(request, 'session/get.html', {'name' :name})

def deleteSession(request):
    if 'name' in request.session:
        del request.session['name']

    return render(request, 'session/del.html')