from ctypes.wintypes import SERVICE_STATUS_HANDLE
try:
    import pygtk
    pygtk.require('2.0')
except:
    print  "*=====================================*"
    print  "*   Install PYGTK from setup files    *"
    print  "*=====================================*"
    exit()
import os
import re
import sys
import time
import threading
import webbrowser
import gtk, gobject
from screen import *
from calenderui import *
from db.dbapi import *

'''
Created on Oct 27, 2015

@author: kristapher
'''           
lock = None

class Order:
    OPEN = 1
    CLOSE = 2
    ATSTORE = 3
    
    def __init__(self, userid, serivceid, whenfrom, whento=None, addId="Home", prefer = None, status = OPEN):
        self.mUserId = userid
        self.mServiceid = serivceid
        self.mWhenFrom = whenfrom
        self.mWhenTo = whento
        self.mAddId = addId
        self.mPrefer = prefer
        self.mStatus = status        

class OrderUI:

    def __init__(self, userinfo):
        self.mUserInfo = userinfo
        self.windowsize = Screen(0, 0, 500, 200)
        self.init_window_layout()
        self.whenfrom = None
        
    #init for UI window layout creation
    def init_window_layout(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.set_resizable(False)
        self.window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse('light gray'))
        self.window.set_title("Order window")        
        #self.window.set_icon_from_file("res"+os.sep+"images"+os.sep+"wwwlogo.png")
        self.window.connect("delete_event", self.delete_event)   
        self.window.connect("destroy", self.destroy)
        self.window.set_size_request(self.windowsize.w, self.windowsize.h)
        


        #***** Menu bar *****#        
        shbox = gtk.HBox(False)
        
        borderimage = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"borderbox.png")
        scaled_buf = pixbuf.scale_simple(self.windowsize.w - 20, self.windowsize.h - 20,gtk.gdk.INTERP_BILINEAR)
        borderimage.set_from_pixbuf(scaled_buf)
        borderimage.show()     
        
        #svbox.set_size_request(600, 300)
        image = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"wwwlogo.png")
        scaled_buf = pixbuf.scale_simple(180,150,gtk.gdk.INTERP_BILINEAR)
        image.set_from_pixbuf(scaled_buf)
        image.show()                

        self.servicecb = gtk.combo_box_entry_new_text()
        self.servicelist = [x[1] for x in DBAPI().get_service_list()]
        print self.servicelist
        for c in self.servicelist:
            self.servicecb.append_text(c)
        self.servicecb.set_active(0)
        self.servicecb.child.connect('changed', self.service_select)        
        
        self.when = gtk.Entry(max=30)
        self.when.set_editable(False)
        self.when.set_size_request(120, 25)
        #self.when.set_text("mm/dd/yy")
        self.calender = gtk.Button()
        timg = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"calender.png")
        scaled_buf = pixbuf.scale_simple(30,18,gtk.gdk.INTERP_BILINEAR)
        timg.set_from_pixbuf(scaled_buf)
        self.calender.add(timg)
        self.calender.connect("clicked", self.setdate_event, "Select date")
        
        self.wherecb = gtk.combo_box_entry_new_text()
        self.addlist = [x[1] for x in DBAPI().get_address_list(self.mUserInfo.mId)]
        print self.addlist
        for c in self.addlist:
            self.wherecb.append_text(c)
        self.wherecb.set_active(0)
        self.wherecb.child.connect('changed', self.address_select)
        
        self.order = gtk.Button()
        self.order.set_label("Order")
        self.order.connect("clicked", self.order_event, "Place order")
        
       
        fix = gtk.Fixed()
        fix.put(borderimage, 10, 10)
        fix.put(image, 40, 25)
        fix.put(self.servicecb, 220, 40)
        fix.put(self.when, 220, 70)
        fix.put(self.calender, 340, 69)
        fix.put(self.wherecb, 220, 100)
        fix.put(self.order, 340, 130)
        
        shbox.add(fix)
        fix.show()
        self.window.add(shbox)
        shbox.show() 
        self.window.show_all() 
   

    def delete_event(self, widget, event, data=None):
        return False
    
    def destroy(self, widget, data=None):
        gtk.main_quit()
        return False
    
    def setdate_event(self, widget, data=None):
        cal = CalendarUI(self.whenfrom)
        cal.main()
        
    def order_event(self, widget, data=None):
        DBAPI().inser_order(Order(self.mUserInfo.mId, self.selectedService, self.whenfrom, addlabel=self.selectedAddress))
        self.window.destroy()        
    
    def service_select(self, entry):
        self.selectedService = self.servicelist.index(entry.get_text())
    
    def address_select(self, entry):
        self.selectedAddress = self.addlist.index(entry.get_text())
        
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
      
     
    