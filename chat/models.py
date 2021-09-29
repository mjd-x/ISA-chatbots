from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=255)
    botInstance = models.IntegerField(null=True, unique=True)

    def __str__(self):
        return self.nombre

class Conversacion(models.Model):
    idUser1 = models.ForeignKey(User, related_name='idUser1', on_delete=models.PROTECT)
    idUser2 = models.ForeignKey(User, related_name='idUser2', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.idUser1) + " + " + str(self.idUser2)

class Mensaje(models.Model):
    mensaje = models.CharField(max_length=255, null=True)
    idUser = models.ForeignKey(User, related_name='sender', on_delete=models.PROTECT)
    idConversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)

    def __str__(self):
        return "(" + str(self.idConversacion) + ") " + str(self.idUser) + ": " + '"' + str(self.mensaje) + '"'