from rest_framework import serializers
from rest_app.models import Blog
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	class Meta:
		model = Blog
		fields = ('id','title','text','created','owner')


class UserSerializer(serializers.ModelSerializer):
	blogs = serializers.PrimaryKeyRelatedField(many=True,queryset=Blog.objects.all())

	class Meta:
		model = User
		fields = ('id','username','blogs')
		
		

