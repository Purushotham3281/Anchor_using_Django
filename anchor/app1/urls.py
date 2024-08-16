from django.urls import path
from  app1 import views
urlpatterns=[
   
    path("Home",views.fun1,name="homepage"),
    path("contact",views.fun2,name="contactpage"),
    path("about",views.fun3,name="aboutpage"),
    path("Help",views.fun4,name="helppage"),
    path("check/<str:string>",views.fun5)

]