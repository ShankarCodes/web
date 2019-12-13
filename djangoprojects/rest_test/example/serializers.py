from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Detail

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
    
class DetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detail
        fields = ['name','address','phone']