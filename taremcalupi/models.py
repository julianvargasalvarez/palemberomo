from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse_lazy

class Address(models.Model):
    limit = Q(model = 'User') | Q(model = 'AffiliateUser')
    addressable_type = models.ForeignKey(ContentType, limit_choices_to=limit)
    addressable_id = models.PositiveIntegerField()
    addressable_object = generic.GenericForeignKey('addressable_type', 'addressable_id')

class CreditCard(models.Model):
    number = models.CharField(max_length=30)

class UserManager(models.Manager):
    def count_the_number_of_users(self):
        return self.all().count()

class User(models.Model):
    email = models.EmailField()  
    name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    objects = UserManager()
    
    def get_absolute_url(self):
        return reverse_lazy('user_update', args=[self.pk])

    def get_absolute_url_for_delete(self):
        return reverse_lazy('user_delete', args=[self.pk])

    @property
    def address(self):
        return Address.objects.get(addressable_type__name='user', addressable_id=self.id)

class AffiliateUser(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  

class AdminUser(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  

class Store(models.Model):
    name = models.CharField(max_length=30)

class StoreLocation(models.Model):
    city = models.CharField(max_length=30)
