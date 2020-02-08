from django.db import models

# Create your models here.

PRIORITY_CHOICES = (
    ('high','High'),
    ('medium','Medium'),
    ('low','Low'),
)

class List(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    list_date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return self.title

