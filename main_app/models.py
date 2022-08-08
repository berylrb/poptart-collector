from django.db import models
from django.urls import reverse

class Poptart(models.Model):
  flavor = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.flavor

  def get_absolute_url(self):
      return reverse("poptarts_detail", kwargs={"poptart_id": self.id})

