from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % (self.name)


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u'%s' % (self.name)
