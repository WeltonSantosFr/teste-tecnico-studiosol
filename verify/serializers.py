from rest_framework import serializers

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    rules = serializers.ListField(child=serializers.DictField())