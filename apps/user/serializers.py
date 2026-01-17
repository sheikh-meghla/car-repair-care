from rest_framework import serializers
from .models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    role = serializers.ChoiceField(choices=CustomUser.Role.choices, default=CustomUser.Role.CUSTOMER)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', CustomUser.Role.CUSTOMER)
        )
        return user
    
class SignInSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True, min_length=6)
        role = serializers.ChoiceField(choices=CustomUser.Role.choices, default=CustomUser.Role.CUSTOMER)

        class Meta:
          model = CustomUser
          fields = ['email', 'password', 'role']

          def create(self, validated_data):
            user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', CustomUser.Role.CUSTOMER)
        )
            
            return user