from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name

class about(models.Model):
    name=models.CharField(max_length=250)
    imaage=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name