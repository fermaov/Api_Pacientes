"""pacientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pacientesAPP import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('pacientes_rest', views.PacienteViewSet)
router.register('tipo_identificacion', views.TipoIdentificacionViewSet)
router.register('sexo_rest', views.SexoViewSet)
router.register('grupo_rh_rest', views.GrupoRhViewSet)
router.register('etnia_rest', views.EtniaViewSet)
router.register('estado_civil_rest', views.EstadoCivilViewSet)
router.register('nivel_educativo_rest', views.NivelEducativoViewSet)
router.register('discapacidad_rest', views.DiscapacidadViewSet)
router.register('municipio_rest', views.MunicipioViewSet)
router.register('departamento_rest', views.DepartamentoViewSet)
router.register('tipo_eapb_rest', views.TipoEapbViewSet)
router.register('eapb_rest', views.EapbViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('tipo_identificacion/<int:pk>/detail/',views.TipoIdentificacionDetailView.as_view(),name='tipo_identificacion-detail'),
    path('sexo/<int:pk>/detail/',views.SexoDetailView.as_view,name='sexo-detail'),
    path('grupo_rh/<int:pk>/detail/',views.GrupoRhDetailView.as_view,name='grupo_rh-detail'),
    path('etnia/<int:pk>/detail/',views.EtniaDetailView.as_view,name='etnia-detail'),
    path('estado_civil/<int:pk>/detail/',views.EstadoCivilDetailView.as_view,name='estado_civil-detail'),
    path('nivel_educativo/<int:pk>/detail/',views.NivelEducativoDetailView.as_view,name='nivel_educativo-detail'),
    path('discapacidad/<int:pk>/detail/',views.DiscapacidadDetailView.as_view,name='discapacidad-detail'),
    path('municipio/<int:pk>/detail/',views.MunicipioDetailView.as_view,name='municipio-detail'),

    #Read
    #path('pacientes/',views.PacienteViewSet.as_view(), name='pacientes-list'),
    # Update
    path('paciente/<int:pk>/update/',views.PacienteUpdate.as_view(),name='paciente-update'), 
    #Create
    path('paciente/create/', views.PacienteCreate.as_view(), name='paciente-create'),
    #Delete
    path('paciente/<int:pk>/delete/', views.PacienteDelete.as_view(), name='paciente-delete'),
    

    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
