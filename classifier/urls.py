from django.urls import path
from .views import PredictObject

urlpatterns = [
    path('predict/', PredictObject.as_view(), name='predict_object'),
]
