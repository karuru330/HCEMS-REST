from django.urls import path
from .views import CategoryAPI, StageAPI, ExpenditureAPI, categoryWiseExpenditureAPI, stageWiseExpenditureAPI

urlpatterns = [
    path('hcems/category', CategoryAPI.as_view()),   
    path('hcems/stage', StageAPI.as_view()),   
    path('hcems/expenditure', ExpenditureAPI.as_view()),
    path('hcems/categoryWiseExpenditure', categoryWiseExpenditureAPI.as_view()), 
    path('hcems/stageWiseExpenditure', stageWiseExpenditureAPI.as_view()),   
]