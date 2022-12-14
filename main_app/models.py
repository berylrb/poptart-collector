from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

FEELINGS = (
  ('R', 'Regret'),
  ('A', 'Ambivalence'),
  ('S', 'Satisfied')
)

class Topping(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toppings_detail', kwargs={'pk': self.id})

class Poptart(models.Model):
  flavor = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  toppings = models.ManyToManyField(Topping)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.flavor

  def get_absolute_url(self):
      return reverse("poptarts_detail", kwargs={"poptart_id": self.id})
    
  def enough_for_today(self):
    return self.emotion_set.filter(date=date.today()).count() >= len(FEELINGS)



class Emotion(models.Model):
  date = models.DateField('Date eaten')
  feeling = models.CharField(
    max_length=1,
    choices=FEELINGS,
    default=FEELINGS[0][0]
    )

  poptart = models.ForeignKey(Poptart, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_feeling_display()} on {self.date}"

  class Meta:
    ordering = ['-date']


