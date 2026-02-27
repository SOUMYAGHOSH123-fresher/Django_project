from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
    def validate(self, validated_data):
        if len(validated_data['username']) < 4:
            raise serializers.ValidationError("Username must be of 5 chracters.")
        
        if len(validated_data['password']) < 5:
            raise serializers.ValidationError("Password must be of 6 characters.")
        
        if not (validated_data['password']).isupper() and isalpha(validated_data['password']):
            raise serializer.ValidationError('Password must have a uppercase letter with symbol')
        
        if '@' not in any(validated_data['email']) or '.' not in any(validated_data['email']):
            raise serializers.ValidationError("Not a valid email")

        return validated_data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email', 'username']
    

class ProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_image']


class ChangeProfilePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

    class Meta:
        model = User
        fields =['old_password', 'new_password']




