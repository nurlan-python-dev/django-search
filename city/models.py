from django.db import models

# Create your models here.
class City(models.Model):
	country = models.CharField(max_length=255, help_text='Mamlakat nomi', verbose_name='Mamlakat')
	iso = models.CharField(max_length=3, help_text='ISO', verbose_name='ISO (Alpha-2 code)')
	city = models.CharField(max_length=255, help_text='Poytaxt', verbose_name='Poytaxt nomi')
	time_zone = models.CharField(max_length=255, help_text='Vaqt zona', verbose_name='Vaqt zonasi')
	class Meta:
		verbose_name = "Shahar "
		verbose_name_plural = "Shaharlar"
	def __str__(self):
		return f'{self.iso} {self.country}'