from django.db import models

# Create your models here.


class techNews(models.Model):
    title = models.CharField(max_length=500)
    img = models.URLField()
    href = models.CharField(max_length=999)
    content = models.TextField()

    def __str__(self):
        return(self.title)
