from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Author
from article.serializers import AuthorSerializer

class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})

    def post(self, request, *args, **kwargs):
        author = Author.objects.create(
            name=request.data["name"],
            email=request.data["email"],
            password=request.data["password"]
        )
        return Response(
            data=AuthorSerializer(author).data
        )
