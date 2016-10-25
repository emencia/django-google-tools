# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GTMCode'
        db.create_table(u'googletools_gtmcode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'googletools', ['GTMCode'])


        # Changing field 'SiteVerificationCode.site'
        db.alter_column(u'googletools_siteverificationcode', 'site_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True))

        # Changing field 'AnalyticsCode.site'
        db.alter_column(u'googletools_analyticscode', 'site_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sites.Site'], unique=True))

    def backwards(self, orm):
        # Deleting model 'GTMCode'
        db.delete_table(u'googletools_gtmcode')


        # Changing field 'SiteVerificationCode.site'
        db.alter_column(u'googletools_siteverificationcode', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True))

        # Changing field 'AnalyticsCode.site'
        db.alter_column(u'googletools_analyticscode', 'site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], unique=True))

    models = {
        u'googletools.analyticscode': {
            'Meta': {'ordering': "('site', 'code')", 'object_name': 'AnalyticsCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'}),
            'speed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'googletools.gtmcode': {
            'Meta': {'ordering': "('site', 'code')", 'object_name': 'GTMCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'googletools.siteverificationcode': {
            'Meta': {'ordering': "('site', 'code')", 'object_name': 'SiteVerificationCode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['sites.Site']", 'unique': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['googletools']