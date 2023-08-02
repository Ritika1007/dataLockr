from rest_framework import serializers
from dataApp.models import *

class SubfolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subfolder
        fields = '__all__'

class JSONFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JSONFile
        fields = "__all__"