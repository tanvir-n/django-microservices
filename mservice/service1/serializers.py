from rest_framework.serializers import ModelSerializer
from .models import Service1

class Service1Serializer(ModelSerializer):
    class Meta:
        model = Service1
        fields = '__all__'