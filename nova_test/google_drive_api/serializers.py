from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
