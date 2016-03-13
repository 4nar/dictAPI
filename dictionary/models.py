from django.db import models

# Create your models here.

class Word(models.Model):
	LANGUAGES = (
		('en', 'english'), 
		('ru', 'russian'),
		('kz', 'kazakh')
		)
	title = models.CharField(max_length=100)
	definition = models.TextField()
	language = models.CharField(max_length=3, choices=LANGUAGES)
	translation = models.ManyToManyField("self", blank=True)
	synonyms = models.ManyToManyField("self", blank=True)
	antonyms = models.ManyToManyField("self", blank=True)

	def __unicode__(self):
	 	return self.title

	