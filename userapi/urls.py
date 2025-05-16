from . import views
from django.urls import path
from .views import DepositHistoryAPI, WithdrawalHistoryAPI
from .views import CreatePaymentView
from .views import payment_ipn


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('deposits/', DepositHistoryAPI.as_view(), name='deposit_history_api'),
    path('withdrawals/', WithdrawalHistoryAPI.as_view(), name='withdrawal_history_api'),
    path('api/create-payment/', CreatePaymentView.as_view(), name='create-payment'),
    path('api/payment-ipn/', payment_ipn, name='payment-ipn'), 
]