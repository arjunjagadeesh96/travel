from. import views
from django.urls import path

urlpatterns = [

    path('',views.ifun,name='ifun'),
    #path('add/',views.addition,name='adition'),
    #path('content/',views.content,name='content')
]