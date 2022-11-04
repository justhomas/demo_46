from rest_framework import viewsets, mixins
from .models import IouUser,Ledger
from .serializers import UserSerializer,LedgerSerializer

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    List of all User objects with details how much they owe and how much they are owed

    Users can be filtered by using their names
    """
    queryset = IouUser.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['name',]

class UserCreateViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    """
    API to create new users

    """   
    queryset = IouUser.objects.all()
    serializer_class = UserSerializer

class IouCreateViewset(viewsets.GenericViewSet,mixins.CreateModelMixin):
    """
    API to add new entries of borrowing

    """ 
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer