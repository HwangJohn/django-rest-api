from .models import Movie
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
 
class MovieList(APIView): 
    """
        영화 리스트 조회
    """
    def get(self, request, format=None):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data, content_type=u"application/json; charset=utf-8")

class MovieAdd(APIView):
    """
        영화 리스트 생성
    """
    @swagger_auto_schema(request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'genre': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'year': openapi.Schema(type=openapi.TYPE_NUMBER, description='integer'),
    }
    ))
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)             

class MovieDetail(APIView):

    def get_object(self, pk):
        try :
            return Movie.objects.get(pk=pk)
        except :
            raise Http404
 
    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)       

    @swagger_auto_schema(request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'genre': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'year': openapi.Schema(type=openapi.TYPE_NUMBER, description='integer'),
    }
    ))
    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
