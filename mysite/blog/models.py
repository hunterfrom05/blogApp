from django.db import models
# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=250) # => This field translate to VARCHAR column in the SQL database.
    slug = models.SlugField(max_length=250) # => This field translate to VARCHAR column in the SQL database. Slug is a short label contains only:[letters,numbers,underscore,hypens]
    body = models.TextField() # => This fiend for storing the body of the post
    def __str__(self):
        # We have add this method to the model class.
        # This is the default python method to return a string with human-readable representaion of the object
        return f'[{self.title}]'

