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

'''
Created on Jan 21, 2015

@author: kristapher
'''           
lock = None

    
class SignupUI:

    def __init__(self):
        self.windowsize = Screen(0, 0, 800, 400)
        self.init_window_layout()
        pass
        
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
        
        self.profilepic = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"profilepictemp.png")
        scaled_buf = pixbuf.scale_simple(200,200,gtk.gdk.INTERP_BILINEAR)
        self.profilepic.set_from_pixbuf(scaled_buf)
        self.profilepic.show()
        
        self.profilepicEdit = gtk.Image()
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"picedit.png")
        scaled_buf = pixbuf.scale_simple(40,40,gtk.gdk.INTERP_BILINEAR)
        self.profilepicEdit.set_from_pixbuf(scaled_buf)
        self.profilepicEdit.show()                            
    
        usernameLabel = gtk.Label()
        usernameLabel.set_label("User Name:")  
        self.mUsername = gtk.Entry(max=30)    
        
        passwdLabel = gtk.Label()
        passwdLabel.set_label("Password:")   
        self.mPassWord = gtk.Entry(max=30)
        
        email = gtk.Label()
        email.set_label("email:")   
        self.mEmail = gtk.Entry(max=30)
        
        AddressLable =  gtk.Label()
        AddressLable.set_label("Address:")   
        self.mAddress = gtk.Entry()
        self.mEmail = gtk.Entry(max=30)
        self.mPassWord.set_visibility(False)
        
        countryLable =  gtk.Label()
        countryLable.set_label("Country:")   
        self.comboboxentry = gtk.combo_box_entry_new_text()
        clist = ["India", "UK", "USA"]
        for c in clist:
            self.comboboxentry.append_text(c)
        self.comboboxentry.child.connect('changed', self.changed_country)
        self.comboboxentry.set_active(0)
        
        state =  gtk.Label()
        state.set_label("State:")   
        self.statecb = gtk.combo_box_entry_new_text()
        clist = ["AP", "TN", "KA"]
        for c in clist:
            self.statecb.append_text(c)
        self.statecb.child.connect('changed', self.state_country)
        self.statecb.set_active(0)
        
        pincodeLabel = gtk.Label()
        pincodeLabel.set_label("PIN:")   
        self.mZIP = gtk.Entry(max=6)
        
        ACLabel = gtk.Label()
        ACLabel.set_label("WWW Area Code:")   
        self.mWWWAC = gtk.Entry(max=6)                
        
        self.register = gtk.Button()
        self.register.set_label("Register")
        self.register.connect("clicked", self.register_event, "Register")

        self.signin = gtk.Button()
        self.signin.set_label("Sign In")
        self.signin.connect("clicked", self.signin_event, "Log in")
        
        fix = gtk.Fixed()
        
        fix.put(borderimage, 10, 10)
        fix.put(image, 40, 25)
        
        fix.put(self.signin, 650, 40)
        
        fix.put(self.profilepic, 150, 130)
        fix.put(self.profilepicEdit, 310, 290)
        
        fix.put(usernameLabel, 400, 130)
        fix.put(self.mUsername, 550, 130)
        
        fix.put(passwdLabel, 400, 160)
        fix.put(self.mPassWord, 550, 160)
        
        fix.put(AddressLable, 400, 190)
        fix.put(self.mAddress, 550, 190)
        
        fix.put(countryLable, 400, 220)
        fix.put(self.comboboxentry, 550, 220)
        
        fix.put(state, 400, 250)
        fix.put(self.statecb, 550, 250)
                       
        fix.put(pincodeLabel, 400, 280)
        fix.put(self.mZIP, 550, 280)
        
        fix.put(ACLabel, 400, 310)
        fix.put(self.mWWWAC, 550, 310)
        
        fix.put(self.register, 640, 340)
        
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
    
    def signin_event(self, widget, data=None):
        self.window.destroy()
        import signinui
        signin = signinui.SigninUI()
        signin.main()
