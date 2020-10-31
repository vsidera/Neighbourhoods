from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import PIL.Image

# Create your models here.
class Neighbourhood(models.Model):
    name=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    population=models.IntegerField()
    picture=CloudinaryField('image')

    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

class Profile(models.Model):
    ''' extended User model '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default='default.png', upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True, default=f'Hello, I am new here!')
    contacts = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = PIL.Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)     

class Business(models.Model):
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE)
    email=models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

class Post(models.Model):
    ''' a model for Project posts '''
    title = models.CharField(max_length=150)
    image = CloudinaryField('image')
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    hood=models.ForeignKey('Neighbourhood',on_delete=models.CASCADE)

