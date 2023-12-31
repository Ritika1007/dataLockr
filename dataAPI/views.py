from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from dataApp.models import Subfolder,JSONFile
from .serializers import SubfolderSerializer,JSONFileSerializer
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema



class SubfolderAPIView(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # queryset = Subfolder.objects.all()
        queryset =  Subfolder.objects.filter(user=request.user).order_by('name')
        serializer = SubfolderSerializer(queryset, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=SubfolderSerializer)
    def post(self, request, format=None):
        serializer = SubfolderSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, pk, format=None):
        try:
            subfolder = Subfolder.objects.get(pk=pk)
            if subfolder.user != request.user:
                return Response({"error": "You do not have permission to delete this subfolder."}, status=status.HTTP_403_FORBIDDEN)
                
            subfolder.delete()
            return Response({"message": "Subfolder deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Subfolder.DoesNotExist:
            return Response({"error": "Subfolder not found."}, status=status.HTTP_404_NOT_FOUND)
        
        
class JSONFileAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_subfolder(self, subfolder_id):
        try:
            return Subfolder.objects.get(pk=subfolder_id)
        except Subfolder.DoesNotExist:
            return None

    def get_file(self, subfolder_id, file_id):
        try:
            subfolder = self.get_subfolder(subfolder_id)
            if subfolder:
                return JSONFile.objects.get(pk=file_id, subfolder=subfolder)
            return None
        except JSONFile.DoesNotExist:
            return None

    def get(self, request, subfolder_id, file_id=None, format=None):
        if file_id is not None:
            # Get details of a specific file in the subfolder
            file_obj = self.get_file(subfolder_id, file_id)
            
            if file_obj:
                if file_obj.subfolder.user != request.user:
                    return Response({"error": "You do not have permission to view this file."}, status=status.HTTP_403_FORBIDDEN)
                serializer = JSONFileSerializer(file_obj)
                return Response(serializer.data)
            return Response({"error": "File not found in the specified subfolder."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # List all files in the subfolder
            subfolder = self.get_subfolder(subfolder_id)
            if subfolder.user != request.user:
                return Response({"error": "You do not have permission to this subfolder."}, status=status.HTTP_403_FORBIDDEN)
              
            if subfolder:
                files = JSONFile.objects.filter(subfolder=subfolder)
                serializer = JSONFileSerializer(files, many=True)
                return Response(serializer.data)
            return Response({"error": "Subfolder not found."}, status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(request_body=JSONFileSerializer)
    def post(self, request, subfolder_id, format=None):
        subfolder = self.get_subfolder(subfolder_id)
        if subfolder.user != request.user:
                return Response({"error": "You do not have permission to create file in this subfolder."}, status=status.HTTP_403_FORBIDDEN)
              
        if subfolder:
            # Pass the subfolder instance to the serializer during creation
            serializer = JSONFileSerializer(data=request.data, context={'subfolder': subfolder})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Subfolder not found."}, status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(request_body=JSONFileSerializer)
    def put(self, request, subfolder_id, file_id, format=None):
        file_obj = self.get_file(subfolder_id, file_id)
        
          
        if file_obj:
            
            if file_obj.subfolder.user != request.user:
                return Response({"error": "You do not have permission to edit this file."}, status=status.HTTP_403_FORBIDDEN)
          
            # Validate and parse the new content as JSON
            try:
                new_content = json.loads(request.data.get('content'))
            except json.JSONDecodeError:
                return Response({"error": "Invalid JSON format"}, status=status.HTTP_400_BAD_REQUEST)

            # Update the file content and save it
            file_obj.content = new_content
            file_obj.save()

            # Serialize the updated file and return the response
            serializer = JSONFileSerializer(file_obj)
            return Response(serializer.data)
        return Response({"error": "File not found in the specified subfolder."}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, subfolder_id, file_id, format=None):
        file_obj = self.get_file(subfolder_id, file_id)
            
        if file_obj:
            if file_obj.subfolder.user != request.user:
                return Response({"error": "You do not have permission to delete this file."}, status=status.HTTP_403_FORBIDDEN)
            
            file_obj.delete()
            return Response({"message": "File deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "File not found in the specified subfolder."}, status=status.HTTP_404_NOT_FOUND)