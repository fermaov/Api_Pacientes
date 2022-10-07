from django.db import models

class Tipo_identificacion(models.Model):
    cod_tipo_iden = models.CharField(max_length=2)
    nom_tipo_iden = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_tipo_iden

class Sexo(models.Model):
    nom_sexo = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_sexo

class Grupo_rh(models.Model):
    nom_grupo_rh = models.CharField(max_length=3)

    def __str__(self):
        return self.nom_grupo_rh

class Etnia(models.Model):
    nom_etnia = models.CharField(max_length=60)

    def __str__(self):
        return self.nom_etnia

class Estado_civil(models.Model):
    nom_estado_civil = models.CharField(max_length=15)

    def __str__(self):
        return self.nom_estado_civil

class Nivel_educativo(models.Model):
    nom_nivel_educativo = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_nivel_educativo

class Discapacidad(models.Model):
    nom_discapacidad = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_discapacidad

class Departamento(models.Model):
    cod_departamento = models.CharField(max_length=2, null=True)
    nom_departamento = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_departamento

class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT)
    cod_municipio = models.CharField(max_length=5, null=True)
    nom_municipio = models.CharField(max_length=30)

    def __str__(self):
        return self.nom_municipio

class Tipo_eapb(models.Model):
    nom_tipo_eapb = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_tipo_eapb

class Eapb(models.Model):
    cod_eapb = models.CharField(max_length=6)
    cod_habilitacion = models.CharField(max_length=12)
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=12)
    nit_dv = models.CharField(max_length=1)
    municipio = models.ForeignKey(Municipio, on_delete=models.RESTRICT, null=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, null=True)
    representante = models.CharField(max_length=100)
    tipo_eapb = models.ForeignKey(Tipo_eapb, on_delete=models.RESTRICT)
    estado = models.CharField(max_length=1,choices=[('A', 'Activo'),('I', 'Inactivo')],default='A')

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    tipo_identificacion = models.ForeignKey(Tipo_identificacion, on_delete=models.RESTRICT)
    nro_identificacion = models.CharField(max_length=15, default='')
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    sexo  = models.ForeignKey(Sexo, on_delete=models.RESTRICT, null=True)
    grupo_rh  = models.ForeignKey(Grupo_rh, on_delete=models.RESTRICT, null=True)
    etnia = models.ForeignKey(Etnia, on_delete=models.RESTRICT, null=True)
    estado_civil = models.ForeignKey(Estado_civil, on_delete=models.RESTRICT, null=True)
    nivel_educativo  = models.ForeignKey(Nivel_educativo, on_delete=models.RESTRICT, null=True)
    discapacidad = models.ForeignKey(Discapacidad, on_delete=models.RESTRICT, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.RESTRICT, null=True)
    direccion = models.CharField(max_length=50, null=True)
    telefono = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)
    eapb = models.ForeignKey(Eapb, on_delete=models.RESTRICT, null=True)
    estado = models.CharField(max_length=1,choices=[('A', 'Activo'),('I', 'Inactivo')],default='A')

    def __str__(self):
        return self.primer_nombre


