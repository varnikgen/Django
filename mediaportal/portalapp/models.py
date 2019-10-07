from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=140)
    slug = models.SlugField()

    def __str__(self):
        return self.name
