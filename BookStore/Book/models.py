from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=120)
    gender=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='bookr')
    date=models.DateTimeField()
    page=models.IntegerField()

    def __str__(self):
        return self.title
