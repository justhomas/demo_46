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
    owed = OwedSerializer(many=True, read_only=True)
    balance = serializers.SerializerMethodField()
    class Meta:
        model = IouUser
        fields = ['name', 'owes', 'owed','balance']

    def get_balance(self,obj):
        total_owes = sum([x.amount for x in obj.owes.all()])
        total_owed = sum([x.amount for x in obj.owed.all()])
        return f"{total_owed - total_owes:1.2f}"


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