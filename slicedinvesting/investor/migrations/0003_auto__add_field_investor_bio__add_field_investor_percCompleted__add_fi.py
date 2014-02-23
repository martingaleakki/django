# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Investor.bio'
        db.add_column(u'investor_investor', 'bio',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Investor.percCompleted'
        db.add_column(u'investor_investor', 'percCompleted',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Investor.pic'
        db.add_column(u'investor_investor', 'pic',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Investor.accountValue'
        db.add_column(u'investor_investor', 'accountValue',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Investor.portfolioValue'
        db.add_column(u'investor_investor', 'portfolioValue',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Investor.followers'
        db.add_column(u'investor_investor', 'followers',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Investor.following'
        db.add_column(u'investor_investor', 'following',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Investor.syndicates'
        db.add_column(u'investor_investor', 'syndicates',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Investor.statusUpdate'
        db.add_column(u'investor_investor', 'statusUpdate',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Investor.portfolioReturn'
        db.add_column(u'investor_investor', 'portfolioReturn',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Investor.joiningDate'
        db.add_column(u'investor_investor', 'joiningDate',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Investor.bio'
        db.delete_column(u'investor_investor', 'bio')

        # Deleting field 'Investor.percCompleted'
        db.delete_column(u'investor_investor', 'percCompleted')

        # Deleting field 'Investor.pic'
        db.delete_column(u'investor_investor', 'pic')

        # Deleting field 'Investor.accountValue'
        db.delete_column(u'investor_investor', 'accountValue')

        # Deleting field 'Investor.portfolioValue'
        db.delete_column(u'investor_investor', 'portfolioValue')

        # Deleting field 'Investor.followers'
        db.delete_column(u'investor_investor', 'followers')

        # Deleting field 'Investor.following'
        db.delete_column(u'investor_investor', 'following')

        # Deleting field 'Investor.syndicates'
        db.delete_column(u'investor_investor', 'syndicates')

        # Deleting field 'Investor.statusUpdate'
        db.delete_column(u'investor_investor', 'statusUpdate')

        # Deleting field 'Investor.portfolioReturn'
        db.delete_column(u'investor_investor', 'portfolioReturn')

        # Deleting field 'Investor.joiningDate'
        db.delete_column(u'investor_investor', 'joiningDate')


    models = {
        u'investor.investor': {
            'Meta': {'object_name': 'Investor'},
            'accountValue': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'followers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'following': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joiningDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'percCompleted': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'portfolioReturn': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'portfolioValue': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'statusUpdate': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'syndicates': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['investor']