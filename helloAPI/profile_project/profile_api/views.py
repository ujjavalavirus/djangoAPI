from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework  import status
from . import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.

"""Hello APIView Class"""
class HelloApiView(APIView):
	"""Test API View."""

	serializer_class = serializers.HelloSerializer


	def get(self, request, format=None):
		"""Returns a list of APIView Features."""

		an_apiview = [
			'Users HTTP methods as function(get, post, patch, put, delete)',
			'It is similar to traiditional django view',
			'Gives you the most control over your logic',
			'Is maapped manually to urls'
		]

		return Response({'message': 'Hello!','api_view': an_apiview})


	def post(self, request):
		"""Create a hello message with our name. """

		serializer =  serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None):
		"""Handles updating on object."""

		return Response({'method': 'put'})

	def patch(self, request, pk=None):
		"""Patch request, only update fields provided in the request"""

		return Response({'method': 'patch'})

	def delete(self, request, pk=None):
		"""Delete an object"""

		return Response({'method': 'Delete'})	



class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet."""

	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Return a hello message."""

		a_viewset = [
			'Uses actions (list, create, update, partical update, Destroy)',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code.',
		]

		return Response({'message': 'Hello!', 'a_viewset': a_viewset})

	def create(self, request):
		"""Create a new hello message."""

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else: 
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		"""Handles getting an object by its ID."""

		return Response({'http_method': 'GET'})


	def update(self, request, pk=None):
		"""Handles updating an object."""

		return Response({'http_method': 'PUT'})

	
	def partial_update(self, request, pk=None):
		"""Handles updating part of an object"""

		return Response({'http_method': 'PATCH'})	


	def destroy(self, request, pk=None):
		"""Handles removing an object."""

		return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handling creating, creating & updating profiles."""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)






