"""
URL configuration for EasyCond project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    #Telas do Menu_Inicial
    path('menu/', menu_views.menu_view, name='menu'),
    #Telas da Solicitação
    path('solicitacao/', solicitacao_views.solicitacao_view, name='solicitacao'),
    #Telas Reserva
    path('reserva/', reserva_views.reserva_view, name='reserva'),
    path('calendario/', reserva_views.calendario_view, name='calendario'),
    path('legenda/', reserva_views.legenda_view, name='legenda'),    
    #Tela Visitas
    path('visitas/', visitas_views.visitas_view, name='visitas'),
    #Tela Denuncia
    path('denuncia/', denuncia_views.denuncia_view, name='denuncia'),
    #Tela Cobranca 
    path('cobranca/', cobranca_views.cobranca_view, name='cobranca'),
]

# ... outras configurações de URL ...

urlpatterns += staticfiles_urlpatterns()