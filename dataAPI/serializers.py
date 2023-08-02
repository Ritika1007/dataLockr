from rest_framework import serializers
from dataApp.models import *

class SubfolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subfolder
        fields = '__all__'

class JSONFileSerializer(serializers.ModelSerializer):
    subfolder_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = JSONFile
        fields = ['id', 'name', 'content', 'subfolder_name']

    def get_subfolder_name(self, obj):
        return obj.subfolder.name if obj.subfolder else None

    def create(self, validated_data):
        subfolder_name = self.context.get('subfolder')
        if subfolder_name:
            subfolder = Subfolder.objects.get(name=subfolder_name)
            validated_data['subfolder'] = subfolder
        return super().create(validated_data)