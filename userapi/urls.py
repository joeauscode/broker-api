from . import views
from django.urls import path
from .views import DepositHistoryAPI, WithdrawalHistoryAPI
from .views import LogoutView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('api/deposits/', DepositHistoryAPI.as_view(), name='deposit_history_api'),
    path('api/withdrawals/', WithdrawalHistoryAPI.as_view(), name='withdrawal_history_api'),
    
   
]