from rest_framework.response import Response
from rest_framework.views import APIView , status
from rest_framework_jwt.settings import api_settings
from django.http import Http404

from article.models import Author
from article.serializers import TokenSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class LoginView(APIView):
    """
    POST auth/login/
    """

    def get_object(self, name, password):
        try:
            return Author.objects.get(name=name, password=password)
        except Author.DoesNotExist:
            return None

    def post(self, request, *args, **kwargs):
        username = request.data.get("name", "")
        password = request.data.get("password", "")
        user = self.get_object(name=username, password=password)

        if user is not None:
            serializer = TokenSerializer(data={
                # using drf jwt utility functions to generate a token
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                ),
                "message": "successfully logged in"
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
