from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PasswordSerializer
from .password_utils import check_password_rules

class PasswordView(APIView):
    def post(self, request):
        serializer = PasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        password = data['password']
        rules = data['rules']
        result = check_password_rules(password, rules)
        return Response(result)