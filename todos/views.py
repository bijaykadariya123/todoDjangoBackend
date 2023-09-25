
# Create your views here.

from .models import Todo
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer

# viewsets has all crud route built in.
class TodoViewSet(viewsets.ModelViewSet):
    # queryset is a list of all Todo object:
    queryset = Todo.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing a deserializing queryset and model instances.
    serializer_class = TodoSerializer
    # Sets Permission_classes to allow unrestricted access to the API
    permissions_classes = [permissions.AllowAny]