# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Wine'
        db.create_table(u'wines_wine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_wines.wine_set', null=True, to=orm['contenttypes.ContentType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'wines', ['Wine'])

        # Adding model 'WhiteWine'
        db.create_table(u'wines_whitewine', (
            (u'wine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wines.Wine'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'wines', ['WhiteWine'])

        # Adding model 'RedWine'
        db.create_table(u'wines_redwine', (
            (u'wine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wines.Wine'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'wines', ['RedWine'])

        # Adding model 'SavignonBlanc'
        db.create_table(u'wines_savignonblanc', (
            (u'whitewine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wines.WhiteWine'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'wines', ['SavignonBlanc'])

        # Adding model 'Merlot'
        db.create_table(u'wines_merlot', (
            (u'redwine_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wines.RedWine'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'wines', ['Merlot'])


    def backwards(self, orm):
        # Deleting model 'Wine'
        db.delete_table(u'wines_wine')

        # Deleting model 'WhiteWine'
        db.delete_table(u'wines_whitewine')

        # Deleting model 'RedWine'
        db.delete_table(u'wines_redwine')

        # Deleting model 'SavignonBlanc'
        db.delete_table(u'wines_savignonblanc')

        # Deleting model 'Merlot'
        db.delete_table(u'wines_merlot')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wines.merlot': {
            'Meta': {'object_name': 'Merlot', '_ormbases': [u'wines.RedWine']},
            u'redwine_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wines.RedWine']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'wines.redwine': {
            'Meta': {'object_name': 'RedWine', '_ormbases': [u'wines.Wine']},
            u'wine_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wines.Wine']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'wines.savignonblanc': {
            'Meta': {'object_name': 'SavignonBlanc', '_ormbases': [u'wines.WhiteWine']},
            u'whitewine_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wines.WhiteWine']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'wines.whitewine': {
            'Meta': {'object_name': 'WhiteWine', '_ormbases': [u'wines.Wine']},
            u'wine_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wines.Wine']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'wines.wine': {
            'Meta': {'object_name': 'Wine'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_wines.wine_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"})
        }
    }

    complete_apps = ['wines']