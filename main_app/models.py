from django.db import models
from django.urls import reverse

FEELINGS = (
  ('R', 'Regret'),
  ('A', 'Ambivalence'),
  ('S', 'Satisfied')
)

class Poptart(models.Model):
  flavor = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.flavor

  def get_absolute_url(self):
      return reverse("poptarts_detail", kwargs={"poptart_id": self.id})



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




