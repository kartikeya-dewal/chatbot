from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from server.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from .functions import botResponse

# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return Response({"something": "my custom JSON"})

    def update(self, request, *args, **kwargs):
        print(request.data)
        res = botResponse(request.data['userText'])
        return Response({"message": res})

