# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Apartment.url'
        db.alter_column(u'apartments_apartment', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Apartment.price'
        db.alter_column(u'apartments_apartment', 'price', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Apartment.date_posted'
        db.alter_column(u'apartments_apartment', 'date_posted', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Apartment.url'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.url' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Apartment.price'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.price' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Apartment.date_posted'
        raise RuntimeError("Cannot reverse this migration. 'Apartment.date_posted' and its values cannot be restored.")

    models = {
        u'apartments.apartment': {
            'Meta': {'object_name': 'Apartment'},
            'bedrooms': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'date_posted': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'postid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'square_feet': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Unchecked'", 'max_length': '20'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['apartments']