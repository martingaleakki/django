# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Investor.lastName'
        db.add_column(u'investor_investor', 'lastName',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Investor.firstName'
        db.alter_column(u'investor_investor', 'firstName', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):
        # Deleting field 'Investor.lastName'
        db.delete_column(u'investor_investor', 'lastName')


        # Changing field 'Investor.firstName'
        db.alter_column(u'investor_investor', 'firstName', self.gf('django.db.models.fields.CharField')(default='', max_length=50))

    models = {
        u'investor.investor': {
            'Meta': {'object_name': 'Investor'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['investor']