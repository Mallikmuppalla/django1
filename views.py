from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta

# Create your views here.
def set_cookie(request):
    response=HttpResponse('<h2>cookie has set</h2>')
    #response.set_cookie('city','Hyderabad',max_age=60)
    response.set_cookie('mycity','GUNTUR',expires=datetime.utcnow()+timedelta(days=3))
    return response
def get_cookie(request):
    #cookie_data=request.COOKIES['city']
    cookie_data=request.COOKIES.get('mycity','THERE IS NO COOKIE RIGHT NOW PLZ SET COOKIE')
    return HttpResponse('cookie data:',cookie_data)
def del_cookie(request):
    responce= HttpResponse('<h2>cookie has deleted</h2>')
    responce.delete_cookie('city')
    return responce
