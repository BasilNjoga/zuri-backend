from django.contrib import admin
from django.urls import include, path
from .views import PersonDetailList, PersonInfo

app_name = "person"

urlpatterns = [
    path("", PersonDetailList.as_view(), name="persons"),
    path("<int:id>/", PersonInfo.as_view()),
]
