from operator import le
from pyexpat import model
from django.db import models

class Author(models.Model):
    name = models.CharField("Name of Author", max_length=100)
    email = models.CharField("Email", max_length=100, blank=True, null=True)
    address = models.TextField("Address", blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()+self.name

class Publication(models.Model):
    name = models.CharField("Name of Publication", max_length=200)
    address = models.TextField("Address", blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()+self.name

class Category(models.Model):
    name = models.CharField("Name", max_length=100)
    desc = models.TextField("Descriptin", null=True, blank=True)

    def __str__(self) -> str:
        return super().__str__()+self.name

class Book(models.Model):
    title = models.CharField("Title", max_length=200)
    author = models.ManyToManyField(Author, verbose_name="Author")
    published_by = models.ForeignKey(Publication, verbose_name="Publication", on_delete=models.SET_NULL, null=True)
    published_at = models.DateField()
    visible_content = models.TextField("Content to be Shown", null=True, blank=True)
    price  = models.FloatField()

    def __str__(self) -> str:
        return super().__str__()+self.title


class Customer(models.Model):
    first_name = models.CharField("First Name", max_length=40)
    last_name = models.CharField("Last Name", max_length=40)
    email = models.CharField("Email", max_length=100)
    GENDER_CHOICES = (
        ("Male", 'Male'),
        ("Female", 'Female'),
    )
    gender = models.CharField("Gender", choices=GENDER_CHOICES, max_length=10, null=True)
    ip = models.CharField("IP Address", max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name