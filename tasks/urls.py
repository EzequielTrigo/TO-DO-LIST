from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.details, name="detail"),
    path("create/", views.createTask, name="create"),
    path("created/", views.createConfirmation, name="created"),
    path("<int:pk>/finish/", views.finish, name="finish"),
]
