from rest_framework import serializers
from .models import CustomUser

# Serializer for creating users
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'role']

    # validate that only admin user can register another admin user, normal user can register only as normal user 
    def validate_role(self, value):
        request = self.context.get('request')

        if request.user.role == "User" and value == "Admin":
            raise serializers.ValidationError(f"Olny admin users have permission to create admin role")
        
        return value
    
    # this is to create user and set password
    def create(self, validated_data):
        password = validated_data.pop("password")

        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user

