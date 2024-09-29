from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.warehouse_home, name='warehouse_home'),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)