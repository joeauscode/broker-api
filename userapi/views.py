from django.shortcuts import render

from rest_framework import serializers,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
from . models import Account
from . serializers import RegistrationSerializer, UserSerializer
from django.db.models import Q
from .models import DepositHistory, WithdrawalHistory

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                response_data = {
                    "first_name": account.first_name,
                    "last_name": account.last_name,
                    "phone": account.phone,
                    "gender": account.gender,
                    "username": account.user.username,
                    "email": account.email,
                }
                return Response(response_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        
# class LoginView(APIView):
#     def post(self, request):
#         try:
#             username = request.data.get('username')
#             password = request.data.get('password')
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return Response({"message": "User logged in successfully!"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)

#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

User = get_user_model()

class LoginView(APIView):
    def post(self, request):
        try:
            login_input = request.data.get('username', '').strip()
            password = request.data.get('password', '')

            if not login_input or not password:
                return Response({"error": "Please provide username/email and password."}, status=status.HTTP_400_BAD_REQUEST)

            user_obj = User.objects.filter(Q(username=login_input) | Q(email=login_input)).first()
            if not user_obj:
                return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

            user = authenticate(username=user_obj.username, password=password)
            if user:
                login(request, user)
                return Response({"message": "User logged in successfully!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid username/email or password."}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class LogoutView(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({"message":"User logout successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
        
            



class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            account = Account.objects.get(user=user)
            user_data = UserSerializer(user).data
            account_data = {
                "account_type": account.account_type,
                "balance": account.balance,
                "created_at": account.created_at,
                # Add more fields from your Account model if needed
            }

            return Response({
                "message": "Dashboard loaded successfully",
                "user": user_data,
                "account": account_data
            }, status=status.HTTP_200_OK)
        
        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class DepositHistoryAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_account = request.user.account  # adjust if necessary
        deposits = DepositHistory.objects.filter(account=user_account).order_by('-timestamp')
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
