from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer

class CommentAPIView(APIView):
    def get(self, _, pk=None):
        comment = Comment.objects.filter(post_id=pk).using('service2')
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CommentSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Create your views here.
