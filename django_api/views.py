from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_api import serializers


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
