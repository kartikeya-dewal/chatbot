from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from server.models import User, Skills
from .serializers import UserSerializer, SkillsSerializer, EducationSerializer
from .functions import botResponse, scoring_metric

# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        userObject = self.get_object()
        serializer = self.get_serializer(userObject)
        userId = serializer.data["id"]
        return Response({"userId": userId})

    def update(self, request, *args, **kwargs):
        print(request.data)
        res = botResponse(request.data["userText"])
        return Response({"message": res})

    def update_user_score(self, request, *args, **kwargs):
        data = scoring_metric(userObject)
        print(data)
        return Response({"data": data})

# Chart Data
class ChartsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        skillsObject = get_object_or_404(Skills, pk=pk)
        data = SkillsSerializer(skillsObject).data

        return Response(data)
