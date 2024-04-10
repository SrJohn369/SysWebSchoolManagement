from django.urls import path
from loginInicio.views import *

app_name = 'loginInicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', login_usuario, name='login_usuario'),
]
