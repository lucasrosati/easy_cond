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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Login import views as login_views
from Cobranca import views as cobranca_views
from Agendamento import views as agendamento_views
from Menu_Inicial import views as menu_views
from Solicitacao import views as solicitacao_views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Telas doLogin
    path('login/', login_views.login_view, name='login'),
    path('cadastro/', login_views.cadastro_view, name='cadastro'),
    path('pagina_de_cadastro/', login_views.pagina_de_cadastro_view, name='pagina_de_cadastro'),

    #Telas do Menu_Inicial
    path('menu/', menu_views.menu_view, name='menu'),

    #Telas da Solicitação
    path('solicitacao/', solicitacao_views.solicitacao_view, name='solicitacao'),
    # Adicione outras URLs conforme necessário, usando os aliases corretos
    # Por exemplo:
    # path('alguma_url/', cobranca_views.nome_da_view, name='nome_da_url'),
    # path('outra_url/', agendamento_views.nome_da_view, name='nome_da_url_2'),
]

# ... outras configurações de URL ...

urlpatterns += staticfiles_urlpatterns()