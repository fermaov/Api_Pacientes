from rest_framework import serializers
from .models import Paciente, Tipo_identificacion, Sexo, Grupo_rh, Etnia, Estado_civil
from .models import Nivel_educativo, Discapacidad, Departamento, Municipio, Eapb, Tipo_eapb

class SexoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sexo
        fields = ('__all__')

class Tipo_identificacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_identificacion
        fields = ('__all__')

class SexoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sexo
        fields = ('__all__')

class Grupo_rhSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Grupo_rh
        fields = ('__all__')

class EtniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Etnia
        fields = ('__all__')

class Estado_civilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estado_civil
        fields = ('__all__')

class Nivel_educativoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nivel_educativo
        fields = ('__all__')

class DiscapacidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discapacidad
        fields = ('__all__')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('__all__')

class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Municipio
        fields = ('__all__')

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ('__all__')

class TipoEapbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo_eapb
        fields = ('__all__')

class EapbSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eapb
        fields = ('__all__')