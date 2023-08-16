from django.urls import path
from .views import CategoryAPI

urlpatterns = [
    path('hcems/addCategory', CategoryAPI.as_view()),   
]