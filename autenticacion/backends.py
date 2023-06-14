from django.contrib.auth.backends import ModelBackend
from autenticacion.models import Administrador, Encargado

class AdministradorBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Administrador.objects.get(username=username)
            if user.check_password(password):
                return user
        except Administrador.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Administrador.objects.get(pk=user_id)
        except Administrador.DoesNotExist:
            return None


class EncargadoBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Encargado.objects.get(username=username)
            if user.check_password(password):
                return user
        except Encargado.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Encargado.objects.get(pk=user_id)
        except Encargado.DoesNotExist:
            return None