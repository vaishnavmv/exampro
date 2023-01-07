
from django.urls import path

from demoapp1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('login_view',views.login_view,name='login_view'),
    path('trainer_register',views.trainer_register,name='trainer_register'),
]
