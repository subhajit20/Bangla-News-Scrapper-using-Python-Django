from django.urls import path
from .views import Scrap

urlpatterns = [
    path('n1/',Scrap)
]
