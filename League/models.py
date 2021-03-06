from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    def save(self):
        self.full_clean()
        super(Player, self).save()


class League(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True)
    league = models.ForeignKey(League)

    def __unicode__(self):
        return u'%s' % (self.name)
