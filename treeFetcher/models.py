from django.db import models

# Create your models here.

class DepCategory(models.Model):
    title = models.CharField(max_length=40)
    discipline_choices = (('UDH', "Hebrew with UD"), ('YAPH', "Hebrew with old dependencies"))
    discipline = models.CharField(max_length=4, choices=discipline_choices, default='UDH')
    description = models.TextField()
    example_sentence = models.CharField(max_length=200)
    example = models.TextField()

    def __str__(self):
        return self.title


class PosCategory(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    example_sentence = models.CharField(max_length=200)
    example = models.TextField()

    def __str__(self):
        return self.title