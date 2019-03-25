from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to = 'galleryToday/')
    image_name = models.CharField(max_length =30)
    image_caption = models.CharField(max_length =30)
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField(max_length =8)
    comments=models.CharField(max_length =100)
    
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()   

    def delete_image(self):
        self.delete()
    
    def update_caption(self):
        self.update()
    

    # @classmethod
    # def search_by_category(cls,search_term):
    #     image_category=Category.objects.filter(name__icontains=search_term)
    #     images = cls.objects.filter(image_category=image_category)
    #     return images 
   
class Profile(models.Model):
    profile_photo = models.CharField(max_length =30)
    bio=models.CharField(max_length =30)

    def __str__(self):
        return self.bio

        

    

# # Create your models here.
# class Image(models.Model):
#     image_name = models.CharField(max_length =30)
#     image_description = models.CharField(max_length =30)
#     image_location = models.ForeignKey(Location)
#     image_category = models.ForeignKey(Category)
#     image = models.ImageField(upload_to = 'galleryToday/')
#     def __str__(self):
#         return self.image_name

#     def save_image(self):
#         self.save()    


#     def delete_image(self):
#         self.delete()

#     class Meta:
#         ordering = ['image_name']    
        
#     @classmethod
#     def get_image(cls,id):
#         try:
#             image=Image.objects.get(id=id)
#             return image
#         except DoesNotExist:
#             return Image.objects.get(id=1)  

#     @classmethod
#     def search_by_category(cls,search_term):
#         image_category=Category.objects.filter(name__icontains=search_term)
#         images = cls.objects.filter(image_category=image_category)
#         return images         
    
#     @classmethod
#     def filter_by_location(cls,filter_term):
#         image_location=Location.objects.filter(name__icontains=filter_term)
#         images = cls.objects.filter(image_location=image_location)
#         return images
  


   