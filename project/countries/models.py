from django.db import models

class Country(models.Model):
    title = models.CharField('Title', max_length=50)
    text = models.TextField('Text')

    class Meta: 
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('title', )

    def __str__(self):
        return self.title


class City(models.Model):
    country = models.ForeignKey(
        Country,
        related_name='cities',
        verbose_name='Country',
        on_delete=models.CASCADE
    )
    title = models.CharField('Title', max_length=50)
    desc = models.TextField('Description', blank=True)

    class Meta: 
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ('title', )

    def __str__(self):
        return self.title

