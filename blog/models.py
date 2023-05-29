from django.db import models
from myapp.models import Usuario
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    data = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    img_url = models.URLField(max_length=500, null=True, blank=True)
    sumary = models.TextField(null=False, blank=False)
    
    
    def __str__(self):
        return self.title
    