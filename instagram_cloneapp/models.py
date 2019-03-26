from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    username=models.CharField(max_length =30)
    profile_photo = models.ImageField(upload_to = 'pic/')
    bio=models.CharField(max_length =30)

    def __str__(self):
        return self.bio

    @classmethod
    def get_picture(cls,id):
        Profile.objects.all()

class Image(models.Model):
    image = models.ImageField(upload_to = 'picture/')
    image_name = models.CharField(max_length =30)
    post = HTMLField()
    image_caption = models.CharField(max_length =30)
    profile = models.ForeignKey(Profile)
    like = models.IntegerField()
    comments=models.CharField(max_length =80)
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()   

    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()
    
    class Meta:
        ordering = ['image_name']  
    # @classmethod
    # def search_by_category(cls,search_term):
    #     image_category=Category.objects.filter(name__icontains=search_term)
    #     images = cls.objects.filter(image_category=image_category)
    #     return images 
   

