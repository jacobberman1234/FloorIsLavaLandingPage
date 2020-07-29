from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    registered = models.DateTimeField(auto_now = True)

    def __str__(self):
       return "{}".format(self.email)