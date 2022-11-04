from rest_framework import viewsets, mixins
from .models import IouUser,Ledger
from .serializers import UserSerializer,LedgerSerializer

# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IouUser.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['name',]

class UserCreateViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = IouUser.objects.all()
    serializer_class = UserSerializer

class IouCreateViewset(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer