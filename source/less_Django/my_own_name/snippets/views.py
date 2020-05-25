from .models import Snippet
from .serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import coreapi
from rest_framework.schemas import AutoSchema

# TODO wykminic, jakie puty wchodza, a jakie nie
# NOTE do swaggera
class MySchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_fields = []
        # if method.lower() == in ["post", "put"]:
        if method.lower() in ["post", "put"]:
            extra_fields = [
                # coreapi.Field(name='desc'),
                # coreapi.Field(name='id', type="integer"),
                coreapi.Field(name='title'),
                coreapi.Field(name='code'),
                coreapi.Field(name='linenos'),
                coreapi.Field(name='language'),
                coreapi.Field(name='style'),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    # NOTE dla swaggera
    schema = MySchema()

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    # NOTE dla swaggera
    schema = MySchema()

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
