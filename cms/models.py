from django.db import models


class Prefecture(models.Model):
    name = models.CharField(verbose_name='県名', max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(verbose_name='名前', max_length=10)
    age = models.PositiveSmallIntegerField()
    prefecture = models.ForeignKey(to='cms.Prefecture',
                                   on_delete=models.CASCADE,
                                   related_name='persons')
