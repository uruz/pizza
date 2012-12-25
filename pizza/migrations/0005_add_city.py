# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.city'
        db.add_column(u'pizza_order', 'city',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Order.city'
        db.delete_column(u'pizza_order', 'city')


    models = {
        u'pizza.component': {
            'Meta': {'object_name': 'Component'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'pizza.deliveryman': {
            'Meta': {'object_name': 'Deliveryman'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'pizza.order': {
            'Meta': {'object_name': 'Order'},
            'address': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'city': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '2'}),
            'deliveryman': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pizza.Deliveryman']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pizza.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pizza.Order']", 'null': 'True', 'blank': 'True'}),
            'pizza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pizza.Pizza']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'pizza.pizza': {
            'Meta': {'object_name': 'Pizza'},
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pizza.Component']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        }
    }

    complete_apps = ['pizza']