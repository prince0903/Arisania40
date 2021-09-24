from django.contrib import admin

# Register your models here.
from .models import Artisan, Atelier

admin.site.register(Artisan)
admin.site.register(Atelier)