# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Order'
        db.create_table(u'pizza_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.TextField')(default='')),
            ('deliveryman', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pizza.Deliveryman'], null=True, blank=True)),
        ))
        db.send_create_signal(u'pizza', ['Order'])

        # Adding model 'OrderItem'
        db.create_table(u'pizza_orderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pizza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pizza.Pizza'], null=True, blank=True)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pizza.Order'], null=True, blank=True)),
        ))
        db.send_create_signal(u'pizza', ['OrderItem'])

        # Adding model 'Deliveryman'
        db.create_table(u'pizza_deliveryman', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal(u'pizza', ['Deliveryman'])


    def backwards(self, orm):
        # Deleting model 'Order'
        db.delete_table(u'pizza_order')

        # Deleting model 'OrderItem'
        db.delete_table(u'pizza_orderitem')

        # Deleting model 'Deliveryman'
        db.delete_table(u'pizza_deliveryman')


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