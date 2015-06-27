#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# WebConfusion activity: A Sugar activity to teach students about Web technologies like HTML,CSS,Javascript.
# Copyright (C) 2015 Vibhor Sehgal 


from gi.repository import Gtk
import logging
import os

from gettext import gettext as _

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.graphics.toolbutton import ToolButton
from sugar3.graphics.toolbarbox import ToolbarButton
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem
from sugar3.presence import presenceservice

from gi.repository import WebKit
import logging
import gconf

from datetime import date




class WebConfusionActivity(activity.Activity):
    

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.max_participants = 1

        self.make_toolbar()
        self.make_mainview()

    
    def make_mainview(self):
        vbox = Gtk.VBox(True) 
        self.webview = webview  = WebKit.WebView()        
	webview.show()
        vbox.pack_start(webview, True, True, 0)
        vbox.show()
	self.swin=Gtk.ScrolledWindow()
	web_app_page = os.path.join(activity.get_bundle_path(), "index.html")
	vbox.scrollable=True
        self.webview.load_uri('file://' + web_app_page)
	self.swin.add_with_viewport(vbox)	
	self.set_canvas(self.swin)
	vbox.show()
	self.swin.show()

    def make_toolbar(self):
        
        toolbar_box = ToolbarBox()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()
	separator=Gtk.SeparatorToolItem(draw=False)
	separator.set_expand(True)
	toolbar_box.toolbar.insert(separator,-1)
	separator.show()
	stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

   	self.set_toolbar_box(toolbar_box)
        toolbar_box.show()
