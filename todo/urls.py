from django.urls import path
from .views import *
urlpatterns = [
    path("task/list/", TaskApiView.as_view()),
    path("task/create/", TaskCreateApiView.as_view()),
    path("task/retrive/update/<int:pk>/", TaskRetriveUpdateApiView.as_view()),
    path("task/destroy/<int:pk>/", TaskDestroyApiView.as_view()),
]