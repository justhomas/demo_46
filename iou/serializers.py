from rest_framework import  serializers
from .models import IouUser,Ledger

class OwesSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Ledger
        fields = ['name','amount']

    def get_name(self,obj):
        return obj.owes.name
class OwedSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
        model = Ledger
        fields = ['name','amount']

    def get_name(self,obj):
        return obj.user.name

class UserSerializer(serializers.ModelSerializer):
    owes = OwesSerializer(many=True, read_only=True)
    owed= OwedSerializer(many=True, read_only=True)
    class Meta:
        model = IouUser
        fields = ['name', 'owes', 'owed']


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ledger
        fields = ['user','owes','amount','expiration']

    def validate(self, data):
        """
        Validatiing if the lender and borrower are same
        """
        lender = data['owes']
        borrower = data['user']
        if lender.name == borrower.name:
            raise serializers.ValidationError("Lender and Borrower cannot be one person")
        return data