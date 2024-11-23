# tasks/models.py
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from pyclamd import pyclamd


class Email(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class Document(models.Model):
    file = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])

    def clean(self):
        cd = pyclamd.ClamdUnixSocket()
        cd.ping()

        result = cd.scan_file(self.file.path)

        if result:
            raise ValueError("File is infected with a virus!")

    def __str__(self):
        return self.file.name