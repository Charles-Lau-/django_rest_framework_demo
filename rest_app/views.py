from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_app.models import Blog
from rest_app.serializers import BlogSerializer,UserSerializer
from django.contrib.auth.models import User



class isOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.owner == request.user
	
class BlogViewSet(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	permission_class = (permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly)
	
	def perform_create(self,serializer):
		serializer.save(owner = self.request.user)
		
class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


