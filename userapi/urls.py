from . import views
from django.urls import path



urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('deposits/', views.DepositHistoryAPI.as_view(), name='deposit_history_api'),
    path('withdrawals/', views.WithdrawalHistoryAPI.as_view(), name='withdrawal_history_api'),
    path('investments/', views.investments_api, name='investments-api'),
    
]




