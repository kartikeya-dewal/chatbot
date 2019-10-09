from rest_framework import serializers
from server.models import User, Education, Skills

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# Education Serializer
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


# Skills Serializer
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"
