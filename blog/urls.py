from django.urls import path, include
from . import views
urlpatterns = [
    path('hello', views.hello, name="hello"),
    path('schedule', views.schedule, name="schedule"),
]