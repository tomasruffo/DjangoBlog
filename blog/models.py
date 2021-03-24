from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	titulo = models.CharField(max_length=100)
	contenido = models.TextField()
	fecha = models.DateTimeField(default= timezone.now)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default="default.jpg", upload_to = "blog_main_picture")

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('post-detail',kwars={'pk':self.pk})

#	def save(self, *args, **kawrgs):
#        super().save(*args,**kawrgs)
#        img = Image.open(self.image.path)



