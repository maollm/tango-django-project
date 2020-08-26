from django.db import models


# Create your models here.
class Category(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.PROTECT)
    # category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

