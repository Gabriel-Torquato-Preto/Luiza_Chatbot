import uuid

from django.db import models


# Create your models here.
class Luiza(models.Model):
    objects = None

    id = models.UUIDField(primary_key=True,  default= uuid.uuid4())
    intents = models.JSONField(null=True)

    def __str__(self) -> str:
        return self.id

class Resposta(models.Model):
    objects = None
    resposta = models.TextField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.id)