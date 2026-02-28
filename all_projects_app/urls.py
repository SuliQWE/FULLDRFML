from django.urls import path
from .views import (StudentPredict, TitanicPredict, HousePredict, BankPredict,
                    DiabetesPredict, AvocadoPredict, MushroomPredict, TelecomPredict)

urlpatterns = [
    path('student_predict/', StudentPredict.as_view(), name='student_predict'),
    path('titanic_predict/', TitanicPredict.as_view(), name='titanic_predict'),
    path('house_predict/', HousePredict.as_view(), name='predict_price'),
    path('bank_predict/', BankPredict.as_view(), name='bank_predict'),
    path('diabetes_predict/', DiabetesPredict.as_view(), name='diabetes_predict'),
    path('avocado_predict/', AvocadoPredict.as_view(), name='avocado_predict'),
    path('mushroom_predict/', MushroomPredict.as_view(), name='mushroom_predict'),
    path('telecom_predict/', TelecomPredict.as_view(), name='telecom_predict'),
]