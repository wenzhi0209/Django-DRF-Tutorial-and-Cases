from dataclasses import Field, field
from pyexpat import model
from django.contrib.auth.models import User,Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        field=['url','username','email','groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        field=['url','name']
    
    