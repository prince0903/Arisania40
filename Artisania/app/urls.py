from . import views
from django.urls import path
app_name='app'
urlpatterns = [
    path('',views.home,name='home'),

]
