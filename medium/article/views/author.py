from rest_framework.response import Response
from rest_framework.views import APIView , status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from article.models import Author
from article.serializers import AuthorSerializer

class AuthorView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})

    def post(self, request, *args, **kwargs):
        author = Author.objects.create(
            username=request.data["username"],
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
            email=request.data["email"],
            password=request.data["password"]
        )
        return Response(
            data=AuthorSerializer(author).data
        )

class AuthorDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AuthorSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AuthorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

