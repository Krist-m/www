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
from  screen import *
import gtk, gobject
from orderui import *
from orderlist import *
from printjob import *
from servicerequestlist import *
#import win32print

'''
Created on Jan 21, 2015

@author: kristapher
'''           
lock = None


class HomeUI:

    def __init__(self, user):
        self.mUserInfo = user
        self.windowsize = Screen(0, 0, 1000, 600)
        self.init_window_layout()

        
    #init for UI window layout creation
    def init_window_layout(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.set_resizable(False)
        self.window.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse('light gray'))
        self.window.set_title("WWW")        
        #self.window.set_icon_from_file("res"+os.sep+"images"+os.sep+"wwwlogo.png")
        self.window.connect("delete_event", self.delete_event)   
        self.window.connect("destroy", self.destroy)
        self.window.set_size_request(self.windowsize.w, self.windowsize.h)
        

        #***** Menu bar *****#        
        shbox = gtk.HBox(False)
        
        borderimage = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"borderbox2.png")
        scaled_buf = pixbuf.scale_simple(self.windowsize.w - 20, self.windowsize.h - 20,gtk.gdk.INTERP_BILINEAR)
        borderimage.set_from_pixbuf(scaled_buf)
        borderimage.show()     
        
        #svbox.set_size_request(600, 300)
        image = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"wwwlogo.png")
        scaled_buf = pixbuf.scale_simple(120,100,gtk.gdk.INTERP_BILINEAR)
        image.set_from_pixbuf(scaled_buf)
        image.show()        
        
        vbox = gtk.VBox(False)
        loader = gtk.gdk.PixbufLoader("png")
        loader.write(self.mUserInfo.mPhoto)
        loader.close()
        pixbuf = loader.get_pixbuf()
        #pixbuf = gtk.gdk.pixbuf_new_from_data(self.mUserInfo.mPhoto,gtk.gdk.COLORSPACE_RGB, False,8,37,29,148)
        #pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"profilepictemp.png")
        scaled_buf = pixbuf.scale_simple(50,50,gtk.gdk.INTERP_BILINEAR)
        self.profilepic = gtk.Image() 
        self.profilepic.set_from_pixbuf(scaled_buf)
        vbox.add(self.profilepic)
        
        username = gtk.Label(self.mUserInfo.mFirstName+" "+self.mUserInfo.mLastName)
        vbox.add(username)
        vbox.show_all()
        
        self.signout = gtk.Button()
        self.signout.set_label("Sign Out")
        self.signout.connect("clicked", self.signout_event, "Logout")
        self.signout.show()
        
        self.newOrder = gtk.Button()
        self.newOrder.set_label("New Order")
        self.newOrder.connect("clicked", self.neworder_event, "Logout")
        self.newOrder.show()
        
        self.mPrint = gtk.Button()
        self.mPrint.set_label("Print")
        self.mPrint.connect("clicked", self.do_print, "Print")
        self.mPrint.show()
        
        self.mOrderList = OrderList()
        self.mServiceList = ServiceRequestList()
        
        notebook = gtk.Notebook()

        scrollview = gtk.ScrolledWindow()
        scrollview.set_size_request(800, 300)
        listview = self.mOrderList.get_view()
        scrollview.add(listview)
        listview.show()
        scrollview.show()
        label = gtk.Label("My Orders")
        notebook.insert_page(scrollview,label )

        scrollview = gtk.ScrolledWindow()
        listview = self.mServiceList.get_view()
        scrollview.add(listview)
        listview.show()
        scrollview.show()
        label = gtk.Label("Service Requests")
        notebook.insert_page(scrollview, label)       
        notebook.show()
                
        fix = gtk.Fixed()        
        fix.put(borderimage, 10, 10)
        fix.put(image, 40, 25)        
        fix.put(self.signout, 900, 50)        
        fix.put(vbox, 840, 40)
        fix.put(notebook, 100, 150)
        fix.put(self.newOrder, 100, 500)
        fix.put(self.mPrint, 200, 500)
        shbox.add(fix)
        
        fix.show()
        self.window.add(shbox)
        shbox.show() 
        self.window.show()
   
    def delete_event(self, widget, event, data=None):
        return False
    
    def destroy(self, widget, data=None):
        gtk.main_quit()
        return False
    
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
    
    def register_event(self, widget, data=None):
        pass
    
    def changed_country(self, entry):
        print entry.get_text()
        return
    
    def state_country(self, entry):
        print entry.get_text()
        return  
    
    def signout_event(self, widget, data=None):
        self.window.destroy()
        import signinui
        signin = signinui.SigninUI()
        signin.main()

    def neworder_event(self, widget, data=None):
        order = OrderUI()
        order.main()
        
        
    def do_print(self, widget, data=None):
        op = OrderPrint()
        
            