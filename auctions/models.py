from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse 


class User(AbstractUser):
    pass

class Listing(models.Model):
	name = models.CharField(max_length=20, help_text='Name of the List Item')
	category=models.ForeignKey('Category', help_text='what category does it falls into', on_delete=models.CASCADE)
	description=models.TextField(blank=True)
	price=models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
	photo=models.ImageField(upload_to="listing")
		
	class Meta:
		order_with_respect_to = 'category'
		
	def get_absolute_url(self):
		return reverse('listing_detail', args=str(self.id))
		
	def __str__(self):
		return self.name

class Category(models.Model):
	name=models.CharField(max_length=20, help_text ='Name of category')
	picture=models.ImageField(upload_to="category", help_text ='picture of this category')
	
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural='categories'
	
	def get_absolute_url(self):
		return reverse('categories')