from django.db import models

class Task(models.Model):
    title= models.CharField(max_length=150)
    description= models.CharField(max_length=500)
    completed= models.BooleanField(default=False)

    def _str_(self):
        return self.title

