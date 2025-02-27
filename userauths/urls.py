from django.urls import path
from userauths import views

urlpatterns =[
    path("sign-up/",views.RegisterView,name="sign-up"),
    path("sign-in/",views.loginView,name="sign-in"),
    path("sign-out/",views.logoutView,name="sign-out"),
]