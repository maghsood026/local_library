from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    name = models.CharField(max_length=32, help_text="Enter genre of book")

    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=32)

    isbn = models.CharField('ISBN', max_length=32, help_text='')

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    genre = models.ManyToManyField(Genre, help_text='select genre to this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ''.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'
class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default= uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length = 1, 
        choices=LOAN_STATUS,
        blank =True,
        null = True,
        default = 'm',
        help_text = 'Book availavilty'
    )


    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    date_of_birthday = models.DateField(null=True, blank=True)

    date_of_death = models.DateField('Die', null=True, blank=True)


    class Meta:
        ordering = ['first_name', 'last_name']


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
