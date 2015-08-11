from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_app.models import Blog
from rest_app.serializers import BlogSerializer,UserSerializer
from django.contrib.auth.models import User


class isOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.owner == request.user
	

class BlogList(generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,isOwnerOrReadOnly)
	queryset = Blog.objects.all()		   
	serializer_class = BlogSerializer

	def perform_create(self,serializer):
		serializer.save(owner = self.request.user)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,isOwnerOrReadOnly,)
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset=  User.objects.all()
	serializer_class =UserSerializer
	
@api_view(('GET',))
def api_root(request,format=None):
	return Response({
			'users':reverse('users-list',request=request,format=format),
			'blogs':reverse('blogs-list',request=request,format=format)
				})
