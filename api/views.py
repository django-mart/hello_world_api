from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer
# Create your views here.

class HelloView(APIView):
    def get(self, request, format=None):
        return Response({"message": "Hello World"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            serializer = HelloSerializer(data=request.data)
            if serializer.is_valid():
                return Response({"message": serializer.data["message"]}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "invalid json data"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except:
            return Response({"message": "Error occured"}, status=status.HTTP_400_BAD_REQUEST)