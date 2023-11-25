from django.urls import path
from .views import CommentAPIView

urlpatterns = [
    path('service2', CommentAPIView.as_view())
    path('service2/<str:pk>/comment', CommentAPIView.as_view())
]