from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,
                                     validators=[
                                         RegexValidator(
                                             regex='^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])[\w@#$%^&+=]{8,}$',
                                             message='пароль должен содержать цифру и спецсимвол и он должен быть не менее 8 символов'
                                         )])
    password_2=serializers.CharField(write_only=True)
    phone_number=serializers.CharField(max_length=13)

    class Meta:
        model = User
        fields = [ 'username', 'email', 'role','password','password_2','phone_number']
        read_only_fields = ['role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_2 = attrs.get('password_2')
        if password != password_2:
            raise serializers.ValidationError("пароли не совпадают")
        return attrs

    def create(self, validated_data):
        user=User(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
