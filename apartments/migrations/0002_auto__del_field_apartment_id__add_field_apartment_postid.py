# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Apartment.id'
        db.delete_column(u'apartments_apartment', u'id')

        # Adding field 'Apartment.postid'
        db.add_column(u'apartments_apartment', 'postid',
                      self.gf('django.db.models.fields.IntegerField')(default=0, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Apartment.id'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.id' and its values cannot be restored.")
        # Deleting field 'Apartment.postid'
        db.delete_column(u'apartments_apartment', 'postid')


    models = {
        u'apartments.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'date_posted': ('django.db.models.fields.DateField', [], {}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'postid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'square_feet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Unchecked'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['apartments']