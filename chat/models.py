from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True)
    botInstance = models.IntegerField(null=True, unique=True)

    def __str__(self):
        return self.name

# class Conversacion(models.Model):
#     idUser1 = models.ForeignKey(User, related_name='idUser1', on_delete=models.PROTECT, null=True)
#     idUser2 = models.ForeignKey(User, related_name='idUser2', on_delete=models.PROTECT, null=True)
#
#     def __str__(self):
#         return str(self.idUser1) + " + " + str(self.idUser2)

class Message(models.Model):
    message = models.CharField(max_length=255, null=True)
    idUser = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True, auto_now_add=True)
    # idConversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return "(" + str(self.idConversacion) + ") " + str(self.idUser) + ": " + '"' + str(self.mensaje) + '"'
        return str(self.idUser) + ": " + '"' + str(self.message) + '"'