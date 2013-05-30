# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'taremcalupi_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('addressable_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('addressable_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'taremcalupi', ['Address'])

        # Adding model 'CreditCard'
        db.create_table(u'taremcalupi_creditcard', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'taremcalupi', ['CreditCard'])

        # Adding model 'User'
        db.create_table(u'taremcalupi_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'taremcalupi', ['User'])

        # Adding model 'AffiliateUser'
        db.create_table(u'taremcalupi_affiliateuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'taremcalupi', ['AffiliateUser'])

        # Adding model 'AdminUser'
        db.create_table(u'taremcalupi_adminuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'taremcalupi', ['AdminUser'])

        # Adding model 'Store'
        db.create_table(u'taremcalupi_store', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'taremcalupi', ['Store'])

        # Adding model 'StoreLocation'
        db.create_table(u'taremcalupi_storelocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'taremcalupi', ['StoreLocation'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'taremcalupi_address')

        # Deleting model 'CreditCard'
        db.delete_table(u'taremcalupi_creditcard')

        # Deleting model 'User'
        db.delete_table(u'taremcalupi_user')

        # Deleting model 'AffiliateUser'
        db.delete_table(u'taremcalupi_affiliateuser')

        # Deleting model 'AdminUser'
        db.delete_table(u'taremcalupi_adminuser')

        # Deleting model 'Store'
        db.delete_table(u'taremcalupi_store')

        # Deleting model 'StoreLocation'
        db.delete_table(u'taremcalupi_storelocation')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taremcalupi.address': {
            'Meta': {'object_name': 'Address'},
            'addressable_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'addressable_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'taremcalupi.adminuser': {
            'Meta': {'object_name': 'AdminUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'taremcalupi.affiliateuser': {
            'Meta': {'object_name': 'AffiliateUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'taremcalupi.creditcard': {
            'Meta': {'object_name': 'CreditCard'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'taremcalupi.store': {
            'Meta': {'object_name': 'Store'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'taremcalupi.storelocation': {
            'Meta': {'object_name': 'StoreLocation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'taremcalupi.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['taremcalupi']