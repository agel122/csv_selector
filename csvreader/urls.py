from django.urls import path
from .views import StartCalc, CountInWork, GetResult, AddResult


urlpatterns = [
    path('start', StartCalc.as_view()),
    path('ongoing', CountInWork.as_view()),
    path('getresult', GetResult.as_view()),
    path('data_adder', AddResult.as_view()),
]