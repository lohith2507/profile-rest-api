from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_api import serializers, models
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django_api import permissions




class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get (self, request, format=None):
        """returns a list of APIView"""
        an_apiview=[
            'Uses HTTP methods as function (get,post,patvh,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you applicationlogic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Updating an object"""
        return Response({'message':'PUT'})

    def patch(self, request, pk=None):
        """Partial Updating an object"""
        return Response({'message':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({"message":"DELETE"})

class HelloViewSet(viewsets.ViewSet):
    """test api viewsets"""
    serializer_class = serializers.HelloSerializer
    def list(self,request):
        """return hello message"""
        a_viewset=[
            'Uses actions (list, create, retrieve, update, partial_upfate)',
            'Automatically maps to URLs using routers',
            'provudes more features with less code'

        ]

        return Response({'message':'Hello', 'a_viewset': a_viewset})
    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        """Handle getting an object by its Id"""
        return Response({'http_method':'Get'})

    def update(self,request, pk = None):
        """Handle updating an object"""
        return Response({'http_method':'Put'})

    def partial_update(self,request, pk = None):
        """Handle partial updating an object"""
        return Response({'http_method':'Patch'})

    def destroy(self,request, pk = None):
        """Handle removing an object"""
        return Response({'http_method':'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
