import uuid as uuid
from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(verbose_name='Pavadinimas', max_length=200, help_text='Iveskite knygos zanra')

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(verbose_name="Vardas", max_length=50)
    last_name = models.CharField(verbose_name="Pavarde", max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=200)
    author = models.ForeignKey(to="Author", on_delete=models.SET_NULL, null=True, blank=True)
    summary = models.TextField(verbose_name='Aprasymas', max_length=1000, help_text='Trumpas knygos aprasymas')
    isbn = models.CharField(verbose_name='ISBN', max_length=13, help_text='13 Simboliu')
    genre = models.ManyToManyField(to='Genre', help_text='Isrinkite zanra(us) siai knygai')

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    uuid = models.UUIDField(verbose_name='Unikalus kodas', default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    book = models.ForeignKey(to="Book", on_delete=models.CASCADE)
    due_back = models.DateField(verbose_name='Grazinimo data', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )

    status = models.CharField(verbose_name='Busena',choices=LOAN_STATUS, default='a', max_length=1, blank=True, )

    def __str__(self):
        return f"{self.uuid} ({self.book.title})"
