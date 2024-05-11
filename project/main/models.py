from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    flavor = models.CharField(max_length=30)
    body = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]