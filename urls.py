from django.urls import path
from cookieapp import views
urlpatterns=[
    path('set/',views.set_cookie),
    path('get/',views.get_cookie),
    path('del/',views.del_cookie),
]

