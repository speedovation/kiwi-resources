#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals, print_function
import sys
import os

from PythonQt import *


def fill_item(item, value):
  item.setExpanded(True)
  if type(value) is dict:
    for key, val in sorted(value.iteritems()):
      child = QTreeWidgetItem()
      child.setText(0, unicode(key))/Volumes/Work/Projects/qt/kiwi/Build/debug/KiWi.app/Contents/MacOS/resources/enrichers/PhpParser/py/php/treeview.py
      item.addChild(child)
      fill_item(child, val)
  elif type(value) is list:
    for val in value:
      child = QTreeWidgetItem()
      item.addChild(child)
      if type(val) is dict:      
        child.setText(0, '[dict]')
        fill_item(child, val)
      elif type(val) is list:
        child.setText(0, '[list]')
        fill_item(child, val)
      else:
        child.setText(0, unicode(val))              
      child.setExpanded(True)
  else:
    child = QTreeWidgetItem()
    child.setText(0, unicode(value))
    item.addChild(child)

def fill_widget(widget, value):
  widget.clear()
  fill_item(widget.invisibleRootItem(), value)
  
  
#  widget = QTreeWidget()
#  fill_widget(widget, d)
#  widget.show()