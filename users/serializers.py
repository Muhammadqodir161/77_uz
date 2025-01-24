from rest_framework import serializers
from .models import User, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name', 'lat', 'long']

class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'full_name', 'role', 'address']

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'full_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data['phone_number'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user
