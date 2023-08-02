from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dataApp.models import Subfolder
from .serializers import SubfolderSerializer


class SubfolderListCreateAPIView(APIView):

    def get(self, request, format=None):
        queryset = Subfolder.objects.all()
        serializer = SubfolderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubfolderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk, format=None):
        try:
            subfolder = Subfolder.objects.get(pk=pk)
            subfolder.delete()
            return Response({"message": "Subfolder deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Subfolder.DoesNotExist:
            return Response({"error": "Subfolder not found."}, status=status.HTTP_404_NOT_FOUND)
    