from django.db import models


class CategoryManager(models.Manager):

    def get_queryset(self):
        return super(CategoryManager, self).get_queryset()

    def filter(self):
        return self.get_queryset().filter(slug='sport')


class Category(models.Model):

    name = models.CharField(max_length=140)
    slug = models.SlugField()
    objects = CategoryManager()

    def __str__(self):
        return self.name
