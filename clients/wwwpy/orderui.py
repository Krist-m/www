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

'''
Created on Jan 21, 2015

@author: kristapher
'''           
lock = None

class OrderUI:

    def __init__(self):
        self.windowsize = Screen(0, 0, 500, 200)
        self.init_window_layout()
        pass

        
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

        self.service = gtk.combo_box_entry_new_text()
        clist = ["Mineral Water (S1)", "Maid (S6)", "Truck (S2)", "Internet (S3)", "Medical Store(S4)", "Bakery d(S6)"]
        for c in clist:
            self.service.append_text(str(c))
        self.service.child.connect('changed', self.service_select)
        self.service.set_active(0)
        
        
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
        
        self.where = gtk.Entry(max=30)
        
        self.order = gtk.Button()
        self.order.set_label("Order")
        self.order.connect("clicked", self.order_event, "Place order")
        
       
        fix = gtk.Fixed()
        fix.put(borderimage, 10, 10)
        fix.put(image, 40, 25)
        fix.put(self.service, 220, 40)
        fix.put(self.when, 220, 70)
        fix.put(self.calender, 340, 69)
        fix.put(self.where, 220, 100)
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
        cal = CalendarUI(self.when)
        cal.main()
        
    def order_event(self, widget, data=None):
        self.window.destroy()
        pass
    
    def service_select(self, entry):
        print entry
    
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
      
     
    