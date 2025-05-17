from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token

from .models import Account, DepositHistory, WithdrawalHistory, Investment, InvestmentHistory
from .serializers import (
    RegistrationSerializer,
    AccountSerializer,
    DepositHistorySerializer,
    InvestmentSerializer,
    InvestmentHistorySerializer,
)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            return Response({
                "message": "Registration successful",
                "user": {
                    "username": account.user.username,
                    "email": account.user.email,
                    "first_name": account.first_name,
                    "last_name": account.last_name,
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        login_input = request.data.get('username', '').strip()
        password = request.data.get('password', '')

        if not login_input or not password:
            return Response({"error": "Please provide username/email and password."},
                            status=status.HTTP_400_BAD_REQUEST)

        user_obj = User.objects.filter(Q(username=login_input) | Q(email=login_input)).first()
        if not user_obj:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(username=user_obj.username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"message": "User logged in successfully!", "token": token.key})
        return Response({"error": "Invalid username/email or password."}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            logout(request)
            return Response({"message": "User logged out successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            account = Account.objects.get(user=user)
        
            account_data = {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "avatar_url": account.avatar.url if account.avatar else None,
                "date_created": account.date_created.strftime('%Y-%m-%d %H:%M:%S'),
                "bitcoin_balance": str(account.bitcoin_balance),
                "ethereum_balance": str(account.ethereum_balance),
                "tron_balance": str(account.tron_balance),
                "doge_balance": str(account.doge_balance),
                "bitcoin_cash_balance": str(account.bitcoin_cash_balance),
                "usdt_trc20_balance": str(account.usdt_trc20_balance),
                "bnb_balance": str(account.bnb_balance),
                "litecoin_balance": str(account.litecoin_balance),
                "usdt_erc20_balance": str(account.usdt_erc20_balance),
                "binance_usd_balance": str(account.binance_usd_balance),
            }
            return Response({"message": "Dashboard loaded successfully", "account": account_data}, status=status.HTTP_200_OK)

        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DepositHistoryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_account = request.user.account
        deposits = DepositHistory.objects.filter(account=user_account).order_by('-timestamp')
        serializer = DepositHistorySerializer(deposits, many=True)
        return Response(serializer.data)
   
    
   



class WithdrawalHistoryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_account = request.user.account
        withdrawals = WithdrawalHistory.objects.filter(account=user_account).order_by('-timestamp')
        data = [
            {
                'timestamp': w.timestamp.isoformat(),
                'crypto': w.crypto,
                'amount': float(w.amount),
                'description': w.description,
            }
            for w in withdrawals
        ]
        return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def investments_api(request):
    investments = Investment.objects.filter(user=request.user)
    serializer = InvestmentSerializer(investments, many=True)
    return Response(serializer.data)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def investment_history_list(request):
    histories = InvestmentHistory.objects.filter(user=request.user)
    serializer = InvestmentHistorySerializer(histories, many=True)
    return Response(serializer.data)










class AvatarUploadView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        user = request.user
        account = Account.objects.get(user=user)
        
        avatar_file = request.data.get('avatar')
        if avatar_file:
            account.avatar = avatar_file
            account.save()
            return Response({"message": "Avatar uploaded successfully", "avatar_url": request.build_absolute_uri(account.avatar.url)}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No avatar file provided"}, status=status.HTTP_400_BAD_REQUEST)
