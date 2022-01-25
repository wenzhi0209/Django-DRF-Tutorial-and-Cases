from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        #fields=['id','title','author','email']
        fields='__all__'
   