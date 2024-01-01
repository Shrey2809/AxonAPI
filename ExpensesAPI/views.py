from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Expenses, Accounts  # Adjust the import path accordingly
from .serializers import ExpensesSerializer, AccountsSerializer  # Adjust the import path accordingly
from drf_spectacular.utils import extend_schema

class ExpensesView(BaseAPIViewSet):
    """
    GET:
        Get all expenses
    """
    @extend_schema(responses={200: ExpensesSerializer(many=True)}, description="Lists all expenses")
    def get(self, request):
        """
        - Retrieves expenses based on query parameters
        - Parameters:
            startIndex (query parameter): The index to start at.
            endIndex    (query parameter): The index to end at.
            category    (query parameter): Filter by category.
            location    (query parameter): Filter by location.
            account     (query parameter): Filter by account.
            date        (query parameter): Filter by date.
        - Responses:
            - 200: Successful response with expenses.
            - 400: Bad request.
            - 403: Forbidden access.
        """
        category = request.query_params.get('category')
        location = request.query_params.get('location')
        account = request.query_params.get('account')
        date = request.query_params.get('date')
        
        expenses = Expenses.objects.all().order_by('id')

        if category:
            expenses = expenses.filter(category=category)
        if location:
            expenses = expenses.filter(location=location)
        if account:
            expenses = expenses.filter(account=account)
        if date:
            expenses = expenses.filter(date=date)

        serializer = ExpensesSerializer(expenses, many=True)
        return Response(serializer.data)
    

    @extend_schema(request=ExpensesSerializer, responses={201: ExpensesSerializer}, description="Create a new expense")
    def post(self, request):
        serializer = ExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=ExpensesSerializer, responses={200: ExpensesSerializer}, description="Update an expense")
    def put(self, request, pk):
        expense = Expenses.objects.get(pk=pk)
        serializer = ExpensesSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=ExpensesSerializer, responses={200: ExpensesSerializer}, description="Update specific fields in an expense")
    def patch(self, request, pk):
        expense = Expenses.objects.get(pk=pk)
        serializer = ExpensesSerializer(expense, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses={204: "No content"}, description="Delete an expense")
    def delete(self, request, pk):
        expense = Expenses.objects.get(pk=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AccountsView(BaseAPIViewSet):
    """
    GET:
        Get all accounts
    """
    @extend_schema(responses={200: AccountsSerializer(many=True)}, description="Lists all accounts")
    def get(self, request):
        """
        - Retrieves accounts based on query parameters
        - Parameters:
            name        (query parameter): Filter by account name.
            balance     (query parameter): Filter by balance.
        - Responses:
            - 200: Successful response with accounts.
            - 400: Bad request.
            - 403: Forbidden access.
        """
        name = request.query_params.get('name')
        balance = request.query_params.get('balance')

        accounts = Accounts.objects.all().order_by('id')

        if name:
            accounts = accounts.filter(name=name)
        if balance:
            accounts = accounts.filter(balance=balance)

        serializer = AccountsSerializer(accounts, many=True)
        return Response(serializer.data)

        @extend_schema(request=AccountsSerializer, responses={201: AccountsSerializer}, description="Create a new account")
    def post(self, request):
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=AccountsSerializer, responses={200: AccountsSerializer}, description="Update an account")
    def put(self, request, pk):
        account = Accounts.objects.get(pk=pk)
        serializer = AccountsSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(request=AccountsSerializer, responses={200: AccountsSerializer}, description="Update specific fields in an account")
    def patch(self, request, pk):
        account = Accounts.objects.get(pk=pk)
        serializer = AccountsSerializer(account, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses={204: "No content"}, description="Delete an account")
    def delete(self, request, pk):
        account = Accounts.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)