from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Task
from .serializers import *
from .paggination import CustomPageNumberPagination
from .filter import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permission import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TaskApiView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter


class TaskCreateApiView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskRetriveUpdateApiView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    lookup_field = "pk"


class TaskDestroyApiView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthorOrReadOnly,]