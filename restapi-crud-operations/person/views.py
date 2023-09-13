from django.shortcuts import render
from .models import PersonDetail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from .serializers import PersonDetailSerializer


class PersonDetailList(APIView):
    def get(self, request):
        obj = PersonDetail.objects.all()
        serializer = PersonDetailSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PersonInfo(APIView):
    def get(self, request, id):
        try:
            obj = PersonDetail.objects.get(id=id)

        except PersonDetail.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonDetailSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = PersonDetail.objects.get(id=id)

        except PersonDetail.DoesNotExist:
            msg = {"msg": "not found error"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonDetailSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = PersonDetail.objects.get(id=id)

        except PersonDetail.DoesNotExist:
            msg = {"msg": "not found error"}

            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = PersonDetailSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = PersonDetail.objects.get(id=id)

        except PersonDetail.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)
