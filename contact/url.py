from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('admin/', admin.site.urls),
    
   
]
