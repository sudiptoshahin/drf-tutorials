from django.urls import path
from . import views


urlpatterns = [
    path('', views.warehouse_home, name='warehouse_home'),
]