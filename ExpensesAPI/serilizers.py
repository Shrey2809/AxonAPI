from rest_framework import serializers
from .models import Expenses, Accounts

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'  # You can specify individual fields if needed

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'  # You can specify individual fields if needed
