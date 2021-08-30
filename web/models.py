from django.db import models

class resume_model(models.Model):
  # img_profile = models.ImageField()
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  description = models.TextField()
  confirmed = models.BooleanField(default=False)
  # abilitys = list