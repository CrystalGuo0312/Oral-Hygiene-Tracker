from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# database model for clinic
class Clinic(models.Model):
	name = models.CharField(default="Clinic", max_length=50)
	address = models.CharField(max_length=100)
	description = models.CharField(max_length=200)
	open_hours = models.CharField(max_length=200)
	phone_number = models.CharField(max_length=12)
	def __str__(self):
		return self.name

# database model for dentist
class Dentist(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=12, default="")
	def __str__(self):
		return self.user.username

# database model for patient
class Patient(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dentist = models.ForeignKey(Dentist, blank=True, null=True, on_delete=models.CASCADE)
	clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.name

# database model for announcement
class Announcement(models.Model):
	dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
	content = models.CharField(default="", max_length=200)
	date_sent = models.DateField(default=timezone.now)
	def __str__(self):
		return self.dentist.user.username + ": " + self.content

# database model for clinic
class Stat(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	has_flossed = models.BooleanField(default=False)
	has_mouth_washed = models.BooleanField(default=False)
	coffee_intake = models.IntegerField(default=0)
	times_brushed = models.IntegerField(default=0)
	sugar_intake = models.IntegerField(default=0)
	date_logged = models.DateField(default=timezone.now)
	def __str__(self):
		return self.patient.user.username + ": " + str(self.date_logged)


###############



'''
# database model for recipe
class Recipe(models.Model):
	recipe_text = models.CharField(max_length = 50)
	recipe_category = models.CharField(max_length = 50)
	recipe_diet_req = models.CharField(max_length = 50, default = "")
	like_count = models.IntegerField(default = 0)
	servings = models.IntegerField(default = 0)
	duration = models.IntegerField(default = 0)
	image_path = models.ImageField(upload_to = 'media/', default = 'recipe_pics/None/no-img.jpg')
	# image_path = models.CharField(max_length = 256)
	chef = models.ForeignKey(Chef, on_delete = models.CASCADE)
	def __str__(self):
		return self.recipe_text

# database model for likes
class Like(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	chef = models.ForeignKey(Chef, on_delete = models.CASCADE)

# database model for recipe ingredients
class Ingredient(models.Model):
	quantity = models.CharField(max_length = 25)
	ingredient_name = models.CharField(max_length = 50)
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	def __str__(self):
		return self.ingredient_name

# database model for recipe steps
class Step(models.Model):
	step_number = models.IntegerField(default = 0)
	contents = models.CharField(max_length = 1024)
	recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
	def __str__(self):
		return self.contents

'''
