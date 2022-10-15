from django.db import models

# Create your models here.
#this inherits from model class "use of inheritance in OOPS". Model is a cloass which is working with a Database
class Project(models.Model):
    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to='portfolio/images/')
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
