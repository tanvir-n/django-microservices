from django.urls import path
from .views import Service1APIView

urlpatterns = [
    path('service1', Service1APIView.as_view())
]