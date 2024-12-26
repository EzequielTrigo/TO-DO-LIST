from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.details, name="detail"),
    #path("<int:pk>/create/", views.create, name="create"),
    path("<int:pk>/finish/", views.finish, name="finish"),
]
