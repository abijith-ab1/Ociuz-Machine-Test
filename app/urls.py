from django.urls import path
from .views import (
    UserListCreateView,
    CategoryListCreateView,
    ExpenseListCreateView,
    ExpenseDetailView,
    MonthlySummaryReportView,
)

urlpatterns = [
    path("users/", UserListCreateView.as_view(), name="user-list-create"),
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("expenses/", ExpenseListCreateView.as_view(), name="expense-list-create"),
    path("expenses/<int:pk>/", ExpenseDetailView.as_view(), name="expense-detail"),
    path("reports/monthly-summary/", MonthlySummaryReportView.as_view(), name="monthly-summary"),
]
