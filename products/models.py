from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=49.99)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def name(self):
        return self.title
