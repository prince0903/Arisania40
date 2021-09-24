from . import views
from django.urls import path
app_name='artisan_app'
urlpatterns = [
    path('list_ateliers/',views.list_atelier,name='list_atelier'),
    path('atelier/<int:atelier_id>',views.detail,name='detail'),

]
