from . import views
from django.urls import path
app_name='compte'
urlpatterns = [
    path('inscription',views.inscriptionPage,name='inscriptionPage'),
    path('login',views.login,name='login')



]
