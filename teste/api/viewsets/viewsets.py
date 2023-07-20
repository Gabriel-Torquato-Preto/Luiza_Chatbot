from rest_framework import viewsets

from ..models import Luiza, Resposta
from ..serializers.serializers import LuizaSerializer, RespostaSerializer


class LuizaViewset(viewsets.ModelViewSet):
    serializer_class = LuizaSerializer
    queryset = Luiza.objects.all()

class RespostaViewset(viewsets.ModelViewSet):
    serializer_class = RespostaSerializer
    queryset = Resposta.objects.all()
