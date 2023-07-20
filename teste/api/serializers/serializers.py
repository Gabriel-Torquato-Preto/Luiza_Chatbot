from rest_framework import serializers
from ..models import Luiza, Resposta

class LuizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Luiza
        fields = '__all__'

class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'

