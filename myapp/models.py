from django.db import models

class Author(models.Model):
    """
    Represents a book author with personal and location details.
    """
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book written by an author.
    """
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    pages = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.title
