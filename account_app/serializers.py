from rest_framework import serializers

from account_app.models import Account


class AccountSerializer(serializers.ModelSerializer): # А ты эту схему используешь в коде ?
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'password', 'posts', 'comments']


class RegisterAccountSerializer(serializers.ModelSerializer):
     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

     class Meta:
         model = Account
         fields = ['email', 'username', 'password', 'password2']
         extra_kwargs = {'password2': {'write_only':True}}

     def create(self, validated_data):
         account = Account(
             email=self.validated_data['email'],
             username=self.validated_data['username'],
         )

         password = self.validated_data['password']
         password2 = self.validated_data['password2']

         if password != password2:
             raise serializers.ValidationError({'password': 'Password must match.'})

         account.set_password(password)
         account.save()
         return account

