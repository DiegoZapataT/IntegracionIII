from djongo import models

class Arquetipos(models.Model):
    tipo = models.IntegerField()
    clave = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    class Meta:
        abstract=True

class Sesiones_medica(models.Model):
    nombre_sesion = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    nombre_profesional = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    centro_salud = models.CharField(max_length=50)
    arquetipos = models.ArrayField(
        model_container=Arquetipos,
        blank = True, 
        default = list
    )

    class Meta:
        abstract=True

class Historial(models.Model):
    _id = models.ObjectIdField()
    dias = models.JSONField()
    casos = models.JSONField()
    objects = models.DjongoManager()

class Arquetipos(models.Model):
    tipo = models.IntegerField()
    clave = models.CharField(max_length=50)
    valor = models.CharField(max_length=50)
    class Meta:
        abstract=True

class Sesiones_medica(models.Model):
    nombre_sesion = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    nombre_profesional = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    centro_salud = models.CharField(max_length=50)
    arquetipos = models.ArrayField(
        model_container=Arquetipos,
        blank = True, 
        default = list
    )

    class Meta:
        abstract=True

class Historial(models.Model):
    _id = models.ObjectIdField()
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    rut = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    fecha_nacimiento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    profesionales_que_atendieron = models.JSONField()
    sesiones_medica = models.ArrayField(
        model_container=Sesiones_medica,
        blank = True, 
        default = list
    )