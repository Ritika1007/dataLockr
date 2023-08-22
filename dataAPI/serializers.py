from rest_framework import serializers
from dataApp.models import *

class SubfolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subfolder
        # fields = '__all__'
        fields = ['id','name']
    
    def create(self, validated_data):
        # Get the currently authenticated user
        user = self.context['request'].user

        # Create the subfolder and associate it with the user
        subfolder = Subfolder.objects.create(user=user, **validated_data)
        return subfolder

class JSONFileSerializer(serializers.ModelSerializer):
    subfolder_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = JSONFile
        fields = ['id', 'name', 'content', 'subfolder_name']

    def get_subfolder_name(self, obj):
        return obj.subfolder.name if obj.subfolder else None
    
    def validate_name(self, value):
        # Check if a file with the given name already exists in the subfolder
        subfolder = self.context.get('subfolder')
        if subfolder and JSONFile.objects.filter(subfolder=subfolder, name=value).exists():
            raise serializers.ValidationError("A file with this name already exists in the subfolder.")
        return value

    def create(self, validated_data):
        subfolder_name = self.context.get('subfolder')
        if subfolder_name:
            subfolder = Subfolder.objects.get(name=subfolder_name)
            validated_data['subfolder'] = subfolder
        return super().create(validated_data)