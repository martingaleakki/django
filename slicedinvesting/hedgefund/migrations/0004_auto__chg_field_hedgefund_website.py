# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HedgeFund.website'
        db.alter_column(u'hedgefund_hedgefund', 'website', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'HedgeFund.website'
        db.alter_column(u'hedgefund_hedgefund', 'website', self.gf('django.db.models.fields.TextField')())

    models = {
        u'hedgefund.hedgefund': {
            'Meta': {'object_name': 'HedgeFund'},
            'assetsUnderManagement': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'capitalRaised': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'capitalRequested': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'completionPerc': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hotness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lockInPeriod': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'managementFees': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'numLikes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'numYearsActive': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'originDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'parentSyndicates': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'performanceFees': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'portfolioManager': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'reportingFrequency': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'returnMetrics': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'website': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['hedgefund']