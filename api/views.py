from rest_framework import generics, permissions
from .serializers import TodoSerialiazer, TodoCompleteSerialiazer
from my_app.models import ToDo
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from django.contrib.auth.models import User


@csrf_exempt
def signup(request):
    if request.method == "POST":
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                data['username'], password=data['password'])
            user.save()
            return JsonResponse({'token': 'dnubdueudew'}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'The username has already been taken! Please chose another username'})


class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerialiazer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = TodoSerialiazer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user, datecompleted__isnull=True).order_by('-datecompleted')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerialiazer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)


class TodoComplete(generics.UpdateAPIView):
    serializer_class = TodoCompleteSerialiazer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.datecompleted = timezone.now()
        serializer.save()
