from django.contrib import admin
from django.urls import include, path
from .views import (
    PersonDetailCreate,
    PersonDetailList,
    PersonDetailDelete,
    PersonDetailUpdate,
    PersonDetails,
)

app_name = "person"

urlpatterns = [
    path("create/", PersonDetailCreate.as_view(), name="create-person"),
    path("", PersonDetailList.as_view()),
    path("<int:pk>/", PersonDetails.as_view(), name="retrieve-person-details"),
    path("<int:pk>/", PersonDetailUpdate.as_view(), name="update-person-details"),
    path("<int:pk>/", PersonDetailDelete.as_view(), name="delete-person"),
]
