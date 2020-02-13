from django.db import models

# Create your models here.


class Position(models.Model):
	title = models.CharField(max_length=200)

	def __str__(self):
		return self.title



class Person(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField(null=True,blank=True)
	image = models.ImageField(upload_to='image/',null=True,blank=True)
	file = models.FileField(upload_to='file/')
	votes = models.IntegerField(blank=True,default=0)
	title = models.ForeignKey(Position,on_delete=models.CASCADE,verbose_name='Running For')

	def __str__(self):
		return self.name



