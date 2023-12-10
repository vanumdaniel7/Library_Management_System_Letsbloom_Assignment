from django.db import models

class Book(models.Model):
    bookId = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 256, null = False)
    author = models.CharField(max_length = 64, null = False)
    edition = models.IntegerField(null = False)
    publisher = models.CharField(max_length = 256, null = False)
    language = models.CharField(max_length = 32, null = False)
    publicationDate = models.DateField(null = False)
    numberOfCopies = models.PositiveBigIntegerField(null = False)

    class Meta:
        unique_together = ('title', 'author', 'edition', 'language', 'publisher')