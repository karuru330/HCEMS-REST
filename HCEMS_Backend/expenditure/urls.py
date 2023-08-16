from django.urls import path
from .views import CategoryAPI

urlpatterns = [
    path('hcems/category', CategoryAPI.as_view()),   
]