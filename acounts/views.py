from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, ProfileSerializer, ProfileImageSerializer, ChangeProfilePasswordSerializer
from .models import Profile
from rest_framework.viewsets import ModelViewSet


from SnippetApp import serializer


# Register API
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "User registered Successfully"}, 
            status=status.HTTP_201_CREATED
        )



# class UserListView(APIView):
#     queryset = User.objects.all()
#     serializer_class = serializer.UserSerializer
#     permission_classes = [AllowAny]



# class UserRetriveView(APIView):
#     queryset = User.objects.all()
#     serializer_class = serializer.UserSerializer






class RegistersView(ModelViewSet):
    queryset=User.objects.all()
    permission_classes=[AllowAny]
    serializer_class=RegisterSerializer

    def perform_create(self, serializer):
        serializer.save()
    


        


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = request.user
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


    def put(self, request):
        profile = request.user
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProfileImageChangeView(APIView):
    permission_classes =[IsAuthenticated]

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer = ProfileImageSerializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


from django.contrib.auth.hashers import check_password

class ProfilePasswordChangeView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self, request):\
        
        serializer = ChangeProfilePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user

            if not check_password(serializer.validated_data['old_password'], user.password):
                return Response({'error': 'Wrong Old password'}, status=400)
        
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password updated successfully"'})
    
        return Response(serializer.errors, status=400)


