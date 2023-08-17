from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)
    category_image = models.ImageField(upload_to="images")


        
class Stage(models.Model):
	stage_name = models.CharField(max_length=50, primary_key=True)
        
class Expenditure(models.Model):
	date_of_expenditure = models.DateField()
	category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
	price = models.IntegerField()
	quantity = models.IntegerField()
	stage_name = models.ForeignKey(Stage, on_delete=models.CASCADE, to_field="stage_name")
	remarks = models.CharField(max_length=500)