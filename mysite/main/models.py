from django.db import models
from datetime import datetime



class Game(models.Model):
	game_name = models.CharField(max_length=200, default=1)
	game_summary = models.CharField(max_length=200)
	game_slug = models.CharField(max_length=200)



	def __str__(self):
		return self.game_name




