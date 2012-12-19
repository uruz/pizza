# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field components on 'Pizza'
        db.create_table(u'pizza_pizza_components', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pizza', models.ForeignKey(orm[u'pizza.pizza'], null=False)),
            ('component', models.ForeignKey(orm[u'pizza.component'], null=False))
        ))
        db.create_unique(u'pizza_pizza_components', ['pizza_id', 'component_id'])


    def backwards(self, orm):
        # Removing M2M table for field components on 'Pizza'
        db.delete_table('pizza_pizza_components')


    models = {
        u'pizza.component': {
            'Meta': {'object_name': 'Component'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'pizza.pizza': {
            'Meta': {'object_name': 'Pizza'},
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['pizza.Component']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        }
    }

    complete_apps = ['pizza']