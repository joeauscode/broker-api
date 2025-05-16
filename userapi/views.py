from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from .models import Account
from . serializers import RegistrationSerializer, UserSerializer
from django.db.models import Q
from .models import DepositHistory, WithdrawalHistory
from rest_framework.authtoken.models import Token
import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponse
import json




class RegisterView(APIView):
    def post(self, request):
        # Deserialize the incoming request data
        serializer = RegistrationSerializer(data=request.data)
        
        # Validate and create user
        if serializer.is_valid():
            account = serializer.save()  # The account is created here
            return Response({
                "message": "Registration successful",
                "user": {
                    "username": account.user.username,
                    "email": account.user.email,
                    "first_name": account.first_name,
                    "last_name": account.last_name
                }
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        login_input = request.data.get('username', '').strip()  # username or email
        password = request.data.get('password', '')

        if not login_input or not password:
            return Response({"error": "Please provide username/email and password."}, status=status.HTTP_400_BAD_REQUEST)

        user_obj = User.objects.filter(Q(username=login_input) | Q(email=login_input)).first()
        if not user_obj:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(username=user_obj.username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"message": "User logged in successfully!", "token": token.key})
        else:
            return Response({"error": "Invalid username/email or password."}, status=status.HTTP_401_UNAUTHORIZED)



class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({"message":"User logout successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def get(self, request):
        try:
            # Get the authenticated user
            user = request.user
            
            # Get the account related to this user
            account = Account.objects.get(user=user)
            
            # Prepare account data with user details
            account_data = {
                "username": user.username,  # Username of the authenticated user
                "first_name": user.first_name,  # User's first name
                "last_name": user.last_name,  # User's last name
                "email": user.email,  # User's email address
                "date_created": account.date_created.strftime('%Y-%m-%d %H:%M:%S'),
                "bitcoin_balance": str(account.bitcoin_balance),  # Convert balance to string to maintain full precision
                "ethereum_balance": str(account.ethereum_balance),
                "tron_balance": str(account.tron_balance),
                "doge_balance": str(account.doge_balance),
                "bitcoin_cash_balance": str(account.bitcoin_cash_balance),
                "usdt_trc20_balance": str(account.usdt_trc20_balance),
                "bnb_balance": str(account.bnb_balance),
                "litecoin_balance": str(account.litecoin_balance),
                "usdt_erc20_balance": str(account.usdt_erc20_balance),
                "binance_usd_balance": str(account.binance_usd_balance),
                # Add other balances as needed
            }

            # Return a success response with the account data
            return Response({
                "message": "Dashboard loaded successfully",
                "account": account_data
            }, status=status.HTTP_200_OK)
        
        except Account.DoesNotExist:
            # If account is not found for the authenticated user
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            # Handle any other exceptions
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
        


class DepositHistoryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_account = request.user.account  # Adjust if necessary
        deposits = DepositHistory.objects.filter(account=user_account).order_by('-timestamp')
        
        # Prepare deposit history data
        data = [
            {
                'timestamp': d.timestamp.isoformat(),
                'crypto': d.crypto,
                'amount': float(d.amount),
                'description': d.description,
            }
            for d in deposits
        ]
        return Response(data)



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












# userapi/views.py






class CreatePaymentView(View):
    def get(self, request):
        headers = {
            'x-api-key': settings.NOWPAYMENTS_API_KEY,
            'Content-Type': 'application/json'
        }

        data = {
            "price_amount": 10,
            "price_currency": "usd",
            "pay_currency": "btc",
            "order_id": "1234",
            "order_description": "Test order",
            "ipn_callback_url": "http://localhost:8000/api/payment-ipn/" 
            
        }

        response = requests.post(
            'https://api.nowpayments.io/v1/payment',
            json=data,
            headers=headers
        )
        
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        try:
            return JsonResponse(response.json())
        except Exception as e:
            return JsonResponse({
                "error": "Failed to parse JSON response",
                "details": str(e),
                "raw_response": response.text
            }, status=500)


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def payment_ipn(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("IPN data received:", data)
        # Process the payment update here
        return HttpResponse('IPN received', status=200)
    return HttpResponse('Method not allowed', status=405)
