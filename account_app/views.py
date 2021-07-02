from rest_framework.response import Response
from rest_framework.views import APIView

from account_app.serializers import AccountSerializer, RegisterAccountSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterAccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():  # тут можно добавить is_valid(raise_exception=True), если не пройдет валидацию будет вызвано исключение и оно обернется в http ответ
            account = serializer.save()
            # Вместо трех строк снизу, стоит создать схему сериалазитора для ответа
            data['respoinse'] = 'succsesful registred account.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)
