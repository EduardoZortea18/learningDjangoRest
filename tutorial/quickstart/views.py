from tutorial.quickstart.models import TaskModel
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

