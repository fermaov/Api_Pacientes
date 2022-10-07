from django.contrib import admin
from .models import Eapb, Tipo_eapb, Tipo_identificacion, Discapacidad, Estado_civil, Etnia, Grupo_rh, Nivel_educativo, Sexo
from .models import Departamento, Municipio, Paciente

admin.site.register(Tipo_identificacion)
admin.site.register(Discapacidad)
admin.site.register(Estado_civil)
admin.site.register(Etnia)
admin.site.register(Grupo_rh)
admin.site.register(Nivel_educativo)
admin.site.register(Sexo)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Paciente)
admin.site.register(Tipo_eapb)
admin.site.register(Eapb)

