from django.urls import path

from . import views

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.event_list, name="list"),
    path("add/", views.add_event, name="add"),
]
