from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.db.models.functions import ExtractYear, ExtractMonth
from django.db.models import Sum
from django.db import connection
from django.contrib.auth.models import User

from .models import Category, Expense
from .serializers import UserSerializer, CategorySerializer, ExpenseSerializer

# Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# Categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    
# Expenses - List + Create
class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user).order_by('-date', '-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

# Monthly Summary Report
class MonthlySummaryReportView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        year = request.query_params.get('year')
        month = request.query_params.get('month')

        if not (year and month):
            return Response({"detail": "year and month are required"}, status=status.HTTP_400_BAD_REQUEST)

        year = int(year)
        month = int(month)

        expenses_by_category = (
            Expense.objects.filter(user=user)
            .annotate(year=ExtractYear("date"), month=ExtractMonth("date"))
            .filter(year=year, month=month)
            .values("category__name")
            .annotate(total_amount=Sum("amount"))
            .order_by("category__name")
        )

        total_expenses = sum(item["total_amount"] for item in expenses_by_category)

        return Response({
            "total_expenses": f"{float(total_expenses):.2f}",
            "expenses_by_category": [
                {
                    "category_name": item["category__name"],
                    "total_amount": f"{float(item['total_amount']):.2f}"
                }
                for item in expenses_by_category
            ]
        })
