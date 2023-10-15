from django.db import models
# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=250) # => this field translate to VARCHAR column in the SQL database.
    slug = models.SlugField(max_length=250) # => this field translate to VARCHAR column in the SQL database. Slug is a short label contains only letters,numbers, underscore, hypens
    title = models.TextField() # => 
    def __str__(self):
        return f'[{self.title}]'

