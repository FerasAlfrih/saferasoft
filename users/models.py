from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=999)
    details = models.TextField(max_length=999)
    startDate = models.DateField()
    deadline = models.DateField()
    salary = models.IntegerField()
    withdrawal = models.IntegerField()
    is_available = models.BooleanField(default=True)

        
    def __str__(self):
        return self.job

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    jobAs = models.OneToOneField(Job, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


