from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from .models import Eapb, Paciente, Tipo_eapb, Tipo_identificacion, Sexo, Grupo_rh, Etnia, Estado_civil
from .models import Nivel_educativo, Discapacidad, Departamento, Municipio
from rest_framework import viewsets
from .serializers import EapbSerializer, PacienteSerializer, Tipo_identificacionSerializer, SexoSerializer, Grupo_rhSerializer, EtniaSerializer, TipoEapbSerializer
from .serializers import Estado_civilSerializer, Nivel_educativoSerializer, DiscapacidadSerializer, DepartamentoSerializer, MunicipioSerializer

class TipoIdentificacionListView(ListView):
    model = Tipo_identificacion

class TipoIdentificacionDetailView(DetailView):
    model = Tipo_identificacion

class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    queryset = Tipo_identificacion.objects.all()
    serializer_class = Tipo_identificacionSerializer

class SexoListView(ListView):
    model = Sexo

class SexoDetailView(DetailView):
    model = Sexo

class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    serializer_class = SexoSerializer

class GrupoRhListView(ListView):
    model = Grupo_rh

class GrupoRhDetailView(DetailView):
    model = Grupo_rh

class GrupoRhViewSet(viewsets.ModelViewSet):
    queryset = Grupo_rh.objects.all()
    serializer_class = Grupo_rhSerializer

class EtniaListView(ListView):
    model = Etnia

class EtniaDetailView(DetailView):
    model = Etnia

class EtniaViewSet(viewsets.ModelViewSet):
    queryset = Etnia.objects.all()
    serializer_class = EtniaSerializer

class EstadoCivilListView(ListView):
    model = Estado_civil

class EstadoCivilDetailView(DetailView):
    model = Estado_civil

class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = Estado_civil.objects.all()
    serializer_class = Estado_civilSerializer

class NivelEducativoListView(ListView):
    model = Nivel_educativo

class NivelEducativoDetailView(DetailView):
    model = Nivel_educativo

class NivelEducativoViewSet(viewsets.ModelViewSet):
    queryset = Nivel_educativo.objects.all()
    serializer_class = Nivel_educativoSerializer

class DiscapacidadListView(ListView):
    model = Discapacidad

class DiscapacidadDetailView(DetailView):
    model = Discapacidad

class DiscapacidadViewSet(viewsets.ModelViewSet):
    queryset = Discapacidad.objects.all()
    serializer_class = DiscapacidadSerializer

class MunicipioListView(ListView):
    model = Municipio

class MunicipioDetailView(DetailView):
    model = Municipio

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all().order_by('nom_municipio')
    serializer_class = MunicipioSerializer

class DepartamentoListView(ListView):
    model = Departamento

class DepartamentoDetailView(DetailView):
    model = Departamento

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all().order_by('nom_departamento')
    serializer_class = DepartamentoSerializer

class PacienteListView(ListView):
    model = Paciente

class PacienteDetailView(DetailView):
    model = Paciente

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = '__all__' 

class PacienteCreate(CreateView):
    model = Paciente
    fields = '__all__'

class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy('paciente-list')

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('nro_identificacion')
    serializer_class = PacienteSerializer

class TipoEapbListView(ListView):
    model = Tipo_eapb

class TipoEapbDetailView(DetailView):
    model = Tipo_eapb

class TipoEapbViewSet(viewsets.ModelViewSet):
    queryset = Tipo_eapb.objects.all()
    serializer_class = TipoEapbSerializer

class EapbListView(ListView):
    model = Eapb

class EapbDetailView(DetailView):
    model = Eapb

class EapbViewSet(viewsets.ModelViewSet):
    queryset = Eapb.objects.all().order_by('nombre')
    serializer_class = EapbSerializer

