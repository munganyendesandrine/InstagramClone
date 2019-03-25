from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.CharField(max_length =30)
    bio=models.CharField(max_length =30)

    def __str__(self):
        return self.bio

class Image(models.Model):
    image = models.ImageField(upload_to = 'galleryToday/')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField()
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
   

