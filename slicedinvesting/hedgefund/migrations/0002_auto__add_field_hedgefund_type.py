# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HedgeFund.type'
        db.add_column(u'hedgefund_hedgefund', 'type',
                      self.gf('django.db.models.fields.CharField')(default='test', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HedgeFund.type'
        db.delete_column(u'hedgefund_hedgefund', 'type')


    models = {
        u'hedgefund.hedgefund': {
            'Meta': {'object_name': 'HedgeFund'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hedgefund']