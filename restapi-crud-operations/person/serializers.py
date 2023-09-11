from rest_framework import serializers
from .models import PersonDetail


class PersonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDetail
        fields = "__all__"
