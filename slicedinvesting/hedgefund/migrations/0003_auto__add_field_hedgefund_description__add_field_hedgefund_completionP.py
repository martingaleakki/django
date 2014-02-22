# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HedgeFund.description'
        db.add_column(u'hedgefund_hedgefund', 'description',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'HedgeFund.completionPerc'
        db.add_column(u'hedgefund_hedgefund', 'completionPerc',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.portfolioManager'
        db.add_column(u'hedgefund_hedgefund', 'portfolioManager',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'HedgeFund.numYearsActive'
        db.add_column(u'hedgefund_hedgefund', 'numYearsActive',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.assetsUnderManagement'
        db.add_column(u'hedgefund_hedgefund', 'assetsUnderManagement',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.managementFees'
        db.add_column(u'hedgefund_hedgefund', 'managementFees',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.performanceFees'
        db.add_column(u'hedgefund_hedgefund', 'performanceFees',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.lockInPeriod'
        db.add_column(u'hedgefund_hedgefund', 'lockInPeriod',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.reportingFrequency'
        db.add_column(u'hedgefund_hedgefund', 'reportingFrequency',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.capitalRequested'
        db.add_column(u'hedgefund_hedgefund', 'capitalRequested',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.capitalRaised'
        db.add_column(u'hedgefund_hedgefund', 'capitalRaised',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.parentSyndicates'
        db.add_column(u'hedgefund_hedgefund', 'parentSyndicates',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'HedgeFund.numLikes'
        db.add_column(u'hedgefund_hedgefund', 'numLikes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.hotness'
        db.add_column(u'hedgefund_hedgefund', 'hotness',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.returnMetrics'
        db.add_column(u'hedgefund_hedgefund', 'returnMetrics',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'HedgeFund.originDate'
        db.add_column(u'hedgefund_hedgefund', 'originDate',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'HedgeFund.website'
        db.add_column(u'hedgefund_hedgefund', 'website',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HedgeFund.description'
        db.delete_column(u'hedgefund_hedgefund', 'description')

        # Deleting field 'HedgeFund.completionPerc'
        db.delete_column(u'hedgefund_hedgefund', 'completionPerc')

        # Deleting field 'HedgeFund.portfolioManager'
        db.delete_column(u'hedgefund_hedgefund', 'portfolioManager')

        # Deleting field 'HedgeFund.numYearsActive'
        db.delete_column(u'hedgefund_hedgefund', 'numYearsActive')

        # Deleting field 'HedgeFund.assetsUnderManagement'
        db.delete_column(u'hedgefund_hedgefund', 'assetsUnderManagement')

        # Deleting field 'HedgeFund.managementFees'
        db.delete_column(u'hedgefund_hedgefund', 'managementFees')

        # Deleting field 'HedgeFund.performanceFees'
        db.delete_column(u'hedgefund_hedgefund', 'performanceFees')

        # Deleting field 'HedgeFund.lockInPeriod'
        db.delete_column(u'hedgefund_hedgefund', 'lockInPeriod')

        # Deleting field 'HedgeFund.reportingFrequency'
        db.delete_column(u'hedgefund_hedgefund', 'reportingFrequency')

        # Deleting field 'HedgeFund.capitalRequested'
        db.delete_column(u'hedgefund_hedgefund', 'capitalRequested')

        # Deleting field 'HedgeFund.capitalRaised'
        db.delete_column(u'hedgefund_hedgefund', 'capitalRaised')

        # Deleting field 'HedgeFund.parentSyndicates'
        db.delete_column(u'hedgefund_hedgefund', 'parentSyndicates')

        # Deleting field 'HedgeFund.numLikes'
        db.delete_column(u'hedgefund_hedgefund', 'numLikes')

        # Deleting field 'HedgeFund.hotness'
        db.delete_column(u'hedgefund_hedgefund', 'hotness')

        # Deleting field 'HedgeFund.returnMetrics'
        db.delete_column(u'hedgefund_hedgefund', 'returnMetrics')

        # Deleting field 'HedgeFund.originDate'
        db.delete_column(u'hedgefund_hedgefund', 'originDate')

        # Deleting field 'HedgeFund.website'
        db.delete_column(u'hedgefund_hedgefund', 'website')


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
            'website': ('django.db.models.fields.TextField', [], {'default': '0'})
        }
    }

    complete_apps = ['hedgefund']