import graphene
from graphene_django import DjangoObjectType
from .models import Ledger,IouUser
from datetime import timezone

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class ExpiredIouType(DjangoObjectType):
    lender = graphene.String()
    borrower = graphene.String()
    class Meta:
        model = Ledger
        fields = ("lender","borrower","amount","expiration")

    def resolve_lender(self,info):
        return self.owes.name

    def resolve_borrower(self,info):
        return self.user.name

class UserType(DjangoObjectType):
    class Meta:
        model = IouUser
        fields = ("name",)

class Query(graphene.ObjectType):
    expired_iou = graphene.List(ExpiredIouType)

    def resolve_expired_iou(root, info):
        return Ledger.objects.all()

      
schema = graphene.Schema(query=Query)