# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Investor'
        db.create_table(u'investor_investor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'investor', ['Investor'])


    def backwards(self, orm):
        # Deleting model 'Investor'
        db.delete_table(u'investor_investor')


    models = {
        u'investor.investor': {
            'Meta': {'object_name': 'Investor'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['investor']