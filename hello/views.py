from django.http import HttpResponse


# def hello(request) :
#     num_visits = request.session.get('num_visits', 0) + 1
#     request.session['num_visits'] = num_visits
#     resp.set_cookie('dj4e_cookie', '75d08d5f', max_age=1000)
#     if num_visits > 4 : del(request.session['num_visits'])
#     return HttpResponse('view count='+str(num_visits))


from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def myview(request):
    # use sessions
    num_visits = request.session.get('num_visits', 0) + 1
    
    request.session['num_visits'] = num_visits 
    
    if num_visits > 4 :
        del(request.session['num_visits'])
    
    response = HttpResponse('view count=' + str(num_visits))
    
    # use cookies
    response.set_cookie('dj4e_cookie', '75d08d5f', max_age=1000)
    
    return response