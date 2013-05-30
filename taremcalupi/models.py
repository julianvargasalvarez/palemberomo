from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Address(models.Model):
    limit = Q(model = 'User') | Q(model = 'AffiliateUser')
    addressable_type = models.ForeignKey(ContentType, limit_choices_to=limit)
    addressable_id = models.PositiveIntegerField()
    addressable_object = generic.GenericForeignKey('addressable_type', 'addressable_id')

class CreditCard(models.Model):
    pass

class UserManager(models.Manager):
    pass

class User(models.Model):
    name = models.CharField(max_length=30)

class AffiliateUser(models.Model):
    pass

class AdminUser(models.Model):
    pass

class Store(models.Model):
    pass

class StoreLocation(models.Model):
    pass
