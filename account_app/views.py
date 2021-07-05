from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail


from account_app import models, serializers, permissions


class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.RegisterAccountSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        # send_mail(message=f'Аккаунт {self.request.data["username"]} с почтовым ящиком {self.request.data["email"]}'
        #                   f' был успешно зарегестрирован',
        #           recipient_list=[self.request.data['email']], from_email=None, subject='Успешная регистрация')
        return Response(status=status.HTTP_201_CREATED, headers=headers)


class AccountsList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer


class GetOneAccount(mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AccountDetailDelete(mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountDetailSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostDetailUpdate(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       generics.GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, permissions.IsOwnerOrReadOnly]
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class LogoutView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)