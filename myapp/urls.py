from django.urls import path
from . import views

urlpatterns = [
    path('index',views.displaymessage,name="welcomeurl"),
    path('home', views.home,name="homeurl"),
    path('personal/<str:name>',views.personal,name="nameurl"),  
    path('homepage/',views.homepage,name="homepageurl"),
    path('aboutus/',views.aboutus,name="abouturl"),
    path('contactus/',views.contactus,name="contacturl"),
    path('header/',views.header,name="header"),
    path('display/<str:fname>/<str:lname>',views.display,name="displayurl"),
    path('insert/<str:nam>/<int:val>',views.insert,name='inserturl'),
    path('display/',views.display,name='display'),
    path('displayform',views.displayform,name="displayformurl"),
    path('displaybyname/<str:nam>',views.displaybyname,name="displaybynameurl"),
    path('displaybyage/<int:age>',views.displaybyage,name="displaybyageurl"),
    path('updatebyid/<int:cid>/<int:ageval>',views.updatebyid,name="updatebyidurl"),
    path('deletebyname/<str:nam>',views.deletebyname,name="deletebynameurl"),
    path('deletebyid/<int:cid>',views.deletebyid,name="deletebyidurl"),
    path('deleteall/',views.deleteall,name="deleteallurl"),
]