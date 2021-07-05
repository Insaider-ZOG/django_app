from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from account_app.models import Account


class RegisterAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ["id", 'email', 'username', 'password', "confirm_password", "date_joined"]

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")
        del attrs['confirm_password']
        attrs['password'] = make_password(attrs['password'])
        return attrs


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'posts', 'comments']
