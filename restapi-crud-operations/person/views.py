from django.shortcuts import render
from .models import PersonDetail
from rest_framework import generics
from .serializers import PersonDetailSerializer


class PersonDetailCreate(generics.CreateAPIView):
    # an API endpoint to allow us to create a new person
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializer


class PersonDetailList(generics.ListAPIView):
    # an API endpoint that allows a person to be viewed
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializer


class PersonDetails(generics.RetrieveAPIView):
    # This API endpoint allows us to return a single persons details by userid
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializer


class PersonDetailUpdate(generics.RetrieveUpdateAPIView):
    # This API endpoint allows a persons details to be updated
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializer


class PersonDetailDelete(generics.RetrieveDestroyAPIView):
    # This API endpoint allows a person to delete a persons details
    queryset = PersonDetail.objects.all()
    serializer_class = PersonDetailSerializer
