from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255,verbose_name='bizimle elaqe')
 
    mail = models.CharField(max_length=255,verbose_name='mail')
    
    subject = models.CharField(max_length=255,verbose_name='movzu')
    mesage = models.CharField(max_length=255,verbose_name='mesage')


    def __str__(self):

     return self.name
    
    class Meta:
       ordering = ('name',) 
       verbose_name = 'bizim haqqimizda'
       verbose_name_plural = 'bizim haqqimizdakilar'

class Products(models.Model):
    card_title = models.CharField(max_length=255,verbose_name='card adi')
    description =models.TextField(verbose_name='bizim haqqimizda')
    image = models.ImageField(upload_to='media/',null=True,blank=True)


    def __str__(self):

     return self.card_title
    
    class Meta:
       ordering = ('card_title',) 
       verbose_name = 'bizim haqqimizda'
       verbose_name_plural = 'bizim haqqimizdakilar'