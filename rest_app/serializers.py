from rest_framework import serializers
from rest_app.models import Blog
from django.contrib.auth.models import User

class BlogSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Blog
		fields = ('id','title','text','created','owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
	blogs = serializers.HyperlinkedRelatedField(many=True,view_name='blog-detail',read_only=True)

	class Meta:
		model = User
		fields = ('id','username','blogs')
		
		

