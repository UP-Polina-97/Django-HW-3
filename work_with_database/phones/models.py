from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.URLField()
    release_data = models.DateField()
    Ite_existe = models.BooleanField()
    slug = models.SlugField(max_length=200)

    def __init__(self):
        return f"{self.id}; {self.name}; {self.price}; {self.image}; {self.release_data}; {self.Ite_existe}; {self.slug}"
