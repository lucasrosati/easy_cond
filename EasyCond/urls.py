from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Login import views as login_views
from Menu_Inicial import views as menu_views
from Solicitacao import views as solicitacao_views
from Reserva import views as reserva_views
from visitas import views as visitas_views
from Denuncia import views as denuncia_views
from Cobranca import views as cobranca_views

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Tela Inicial (definida como a tela de cadastro)
    path('', login_views.cadastro_view, name='cadastro'),
    # Telas do Login
    path('pagina_de_login/', login_views.pagina_de_login_view, name='pagina_de_login'),
    path('cadastro/', login_views.cadastro_view, name='cadastro'),
    path('pagina_de_cadastro/', login_views.cadastro_usuario, name='pagina_de_cadastro'),
    path('login/', login_views.CustomLoginView.as_view(), name='login'),  # Use apenas a sua visualização personalizada

    # Rota para redirecionar após o login bem-sucedido
    path('menu/', menu_views.menu_view, name='menu'),
    # Telas do Menu_Inicial
    path('menu/', menu_views.menu_view, name='menu'),
    # Telas da Solicitação
    path('solicitacao/', solicitacao_views.solicitacao_view, name='solicitacao'),
    # Telas Reserva
    path('reserva/', reserva_views.reserva_view, name='reserva'),
    path('calendario/', reserva_views.calendario_view, name='calendario'),
    path('legenda/', reserva_views.legenda_view, name='legenda'),
    # Tela Visitas
    path('visitas/', visitas_views.visitas_view, name='visitas'),
    # Tela Denuncia
    path('denuncia/', denuncia_views.denuncia_view, name='denuncia'),
    # Tela Cobrança 
    path('cobranca/', cobranca_views.cobranca_view, name='cobranca'),
    path('verificar_usuario/', login_views.verificar_usuario, name='verificar_usuario'),
]

# ... outras configurações de URL ...

urlpatterns += staticfiles_urlpatterns()
