from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout"),
    path('signup', views.signup, name='signup'),
    path('addmo', views.addmo, name='addmo'),
    path('outs', views.outs, name='outs'),
    path('Brief', views.Brief, name='Brief'),    
]
