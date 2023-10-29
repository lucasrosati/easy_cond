from django.test import TestCase

from Login.models import UserProfile 


class UserProfile(TestCase):

    def setUp(self):

        nome = "RonaldoJacaré"
        nome_usuario = "ronaldotsm"
        apartamento = "1702"
        tipo_usuario = "MORADOR"
        senha = "12345678"
        self.perfil_user = UserProfile(nome, nome_usuario, apartamento, tipo_usuario, senha)


        