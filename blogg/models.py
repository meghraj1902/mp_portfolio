from django.db import models

# Create your models here.
class Blogg(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField()
    #imageb = models.ImageField(upload_to='portfolio/images/')
    #url = models.URLField(blank=True)
    def __str__(self):
        return self.title
