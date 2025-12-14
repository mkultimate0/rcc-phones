from django.db import models

# Create your models here.

class Division(models.Model):
	title = models.CharField("Подразделение", max_length=150)

	def __str__(self):
		return self.title

class Persone(models.Model):
	# pk/id
	name = models.CharField("ФИО сотрудника", max_length=50)
	division = models.ForeignKey(
		Division,
		on_delete=models.PROTECT, 
		null=True, 
		verbose_name='Подразделение')
	note = models.TextField(blank=True, verbose_name="примечание")  # поле "примечание"

	def __str__(self):
		return self.name

class Phone(models.Model):
	phone = models.CharField("Вн. номер", max_length=50)
	contact = models.ForeignKey(
		Persone,
		on_delete=models.CASCADE, 
		related_name="phones")
	
	def __str__(self):
		return self.phone
	