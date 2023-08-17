from django.urls import path
from .views import CategoryAPI, StageAPI, ExpenditureAPI

urlpatterns = [
    path('hcems/category', CategoryAPI.as_view()),   
    path('hcems/stage', StageAPI.as_view()),   
    path('hcems/expenditure', ExpenditureAPI.as_view()),   
]