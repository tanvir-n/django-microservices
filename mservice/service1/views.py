from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Service1Serializer
from .models import Service1
import requests


class Service1APIView(APIView):
    def get(self, request):
        service1 = Service1.objects.all().using('service1')
        serializer = Service1Serializer(service1, many=True)
        return Response(self.formatPost(p) for p in serializer.data)

    def formatPost(self, post):
        comment = requests.get('http://127.0.0.1:8000/service2/service2/%d/comment' % post.id).json()
        return {
            'id': post.id,
            'title': post.title,
            'des': post.desc,
            'comment': comment 
        }

    def post(self, request):
        serializer = Service1Serializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)