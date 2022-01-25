
from multiprocessing import AuthenticationError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer

from rest_framework.views import APIView

from rest_framework import generics

#from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
#from rest_framework.permissions import IsAuthenticated

from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()




class GenericAPIView(generics.ListAPIView):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()


class GenericAPIViewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=ArticleSerializer
    queryset=Article.objects.all()



class ArticleAPIView(APIView):

    def get(self,request):
        articles = Article.objects.all()
        serializer= ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ArticleDetails(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(pk=id)
    
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        serializer= ArticleSerializer(self.get_object(id=id))
        return Response(serializer.data)
    
    def put(self,request,id):
        serializer=ArticleSerializer(self.get_object(id=id),data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        self.get_object(id=id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





@api_view(['GET', 'POST'])
def article_list(request):
    if  request.method =='GET':
        articles = Article.objects.all()
        serializer= ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request,pk1):
    try:
        article= Article.objects.get(pk=pk1)
    
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer= ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method  =='PUT':
        serializer=ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    elif request.method =='DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)