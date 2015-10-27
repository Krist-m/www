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
from db.dbapi import *
from user import *
from address import *

'''
Created on Jan 21, 2015

@author: kristapher
'''           
lock = None

    
class SignupUI:

    def __init__(self):
        self.windowsize = Screen(0, 0, 800, 600)
        self.init_window_layout()
        self.misServiceProvider = False
        self.mServiceName = None
        self.mPhotoPath = "res"+os.sep+"images"+os.sep+"profilepictemp.png"
        
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
        
        ebox = gtk.EventBox()
        profilepicEdit = gtk.Image()
        ebox.connect("button-press-event", self.edit_profile_pic)
        pixbuf = gtk.gdk.pixbuf_new_from_file("res"+os.sep+"images"+os.sep+"picedit.png")
        scaled_buf = pixbuf.scale_simple(40,40,gtk.gdk.INTERP_BILINEAR)
        profilepicEdit.set_from_pixbuf(scaled_buf)
        profilepicEdit.show()  
        ebox.add(profilepicEdit)                            
    
        phonenoLabel = gtk.Label("Phoneno:")
        self.mPhoneno = gtk.Entry(max=30)    
        
        firstnameLabel = gtk.Label("First name:")
        self.mFirstName = gtk.Entry(max=30)    
        lastnameLabel = gtk.Label("Last name:")
        self.mLastName = gtk.Entry(max=30)    
                
        passwdLabel = gtk.Label("Password:")
        self.mPassWord = gtk.Entry(max=30)
        self.mPassWord.set_visibility(False)
        
        email = gtk.Label("email:")
        self.mEmail = gtk.Entry(max=30)
        
        AddressLable =  gtk.Label("Home Address:")
        houseNoLabel =  gtk.Label("house no.:")
        self.mHouseNo = gtk.Entry()
        streetLabel =  gtk.Label("Street:")
        self.mStreet = gtk.Entry()
        
        cityLabel =  gtk.Label("City:")
        self.mCity = gtk.Entry()
        
        countryLable =  gtk.Label("Country:")
        self.comboboxentry = gtk.combo_box_entry_new_text()
        clist = ["India", "UK", "USA"]
        for c in clist:
            self.comboboxentry.append_text(c)
        self.comboboxentry.child.connect('changed', self.changed_country)
        self.comboboxentry.set_active(0)
        
        state =  gtk.Label("State:")
        self.statecb = gtk.combo_box_entry_new_text()
        clist = ["AP", "TN", "KA"]
        for c in clist:
            self.statecb.append_text(c)
        self.statecb.child.connect('changed', self.changed_state)
        self.statecb.set_active(0)
        
        pincodeLabel = gtk.Label("PIN:")
        self.mZIP = gtk.Entry(max=6)
        
        ACLabel = gtk.Label("WWW Area Code:")
        self.mWWWAC = gtk.Entry(max=6)                
        self.serviceprovider = gtk.CheckButton("  Service Provider")
        self.serviceprovider.connect("toggled", self.event_serviceprovider, "RPW")  
        
        self.register = gtk.Button("Register")
        self.register.connect("clicked", self.register_event, "Register")

        self.signin = gtk.Button("Sign In")
        self.signin.connect("clicked", self.signin_event, "Log in")
        
        self.fix = gtk.Fixed()
        
        self.fix.put(borderimage, 10, 10)
        self.fix.put(image, 40, 25)
        
        self.fix.put(self.signin, 670, 35)
        
        self.fix.put(self.profilepic, 150, 130)
        self.fix.put(ebox, 310, 290)
        
        
        self.fix.put(phonenoLabel, 400, 70)
        self.fix.put(self.mPhoneno, 530, 70)
        
        self.fix.put(firstnameLabel, 400, 100)
        self.fix.put(self.mFirstName, 530, 100)
        self.fix.put(lastnameLabel, 400, 130)
        self.fix.put(self.mLastName, 530, 130)
        
        
        self.fix.put(passwdLabel, 400, 160)
        self.fix.put(self.mPassWord, 530, 160)
        
        self.fix.put(AddressLable, 400, 190)        
        self.fix.put(houseNoLabel, 400, 220)
        self.fix.put(self.mHouseNo, 530, 220)
        self.fix.put(streetLabel, 400, 250)
        self.fix.put(self.mStreet, 530, 250)
        
        self.fix.put(countryLable, 400, 280)
        self.fix.put(self.comboboxentry, 530, 280)
        
        self.fix.put(state, 400, 310)
        self.fix.put(self.statecb, 530, 310)
        
        self.fix.put(cityLabel, 400, 340)
        self.fix.put(self.mCity,530, 340)
                       
        self.fix.put(pincodeLabel, 400, 370)
        self.fix.put(self.mZIP, 530, 370)
        
        self.fix.put(ACLabel, 400, 400)
        self.fix.put(self.mWWWAC, 530, 400)
        
        self.fix.put(self.serviceprovider, 400, 430)
        
        self.fix.put(self.register, 622, 495)
        
        shbox.add(self.fix)
        
        self.fix.show()
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
        mypic = open(self.mPhotoPath, 'rb').read()
        user = User(self.mFirstName.get_text(), self.mLastName.get_text(), self.mPassWord.get_text(),
                    self.mPhoneno.get_text(), mypic, self.misServiceProvider, self.mServiceName)
            
        address = Address(self.mHouseNo.get_text(), self.mStreet.get_text(), 
                          self.mCity.get_text(), self.mState, self.mCountry, self.mZIP.get_text(), label="Home", areacode=self.mWWWAC.get_text())
        db = DBAPI()
        id = db.insert_user_info(user)
        db.insert_address(id, address)
        self.signin_event()     
        
    def changed_country(self, entry):
        self.mCountry = entry.get_text()

    
    def changed_state(self, entry): 
        self.mState = entry.get_text()
    
    def signin_event(self, widget=None, data=None):
        self.window.destroy()
        import signinui
        signin = signinui.SigninUI()
        signin.main()
    
    def edit_profile_pic(self, widget=None, data=None):
        print "edit_profile_pic"
        dialog = gtk.FileChooserDialog( "Select photo...",
                               None,
                               gtk.FILE_CHOOSER_ACTION_OPEN,
                               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                               gtk.STOCK_APPLY, gtk.RESPONSE_APPLY))
        dialog.set_default_response(gtk.RESPONSE_OK)
        
        dialog.set_current_folder(os.getcwd())        

        filter = gtk.FileFilter()
        filter.add_pattern("*.png")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == gtk.RESPONSE_APPLY:
            self.mPhotoPath = dialog.get_filename()
            dialog.destroy()
            file = open(self.mPhotoPath, "rb")
            binary = file.read()
            loader = gtk.gdk.PixbufLoader("png")
            loader.write(binary)
            loader.close()
            pixbuf = loader.get_pixbuf()
            scaled_buf = pixbuf.scale_simple(200,200,gtk.gdk.INTERP_BILINEAR)
            self.profilepic.set_from_pixbuf(scaled_buf)
            self.profilepic.show()

    def event_serviceprovider(self, widget=None, data=None):
        print "event_serviceprovider"
        if widget.get_active():
            servicelabel = gtk.Label("Service item:")
            self.servicecb = gtk.combo_box_entry_new_text()
            self.servicelist = [x[1] for x in DBAPI().get_service_list()]
            print self.servicelist
            for c in self.servicelist:
                self.servicecb.append_text(c)
            self.servicecb.set_active(0)
            self.servicecb.child.connect('changed', self.selete_service)
            self.fix.put(servicelabel, 400, 460)
            self.fix.put(self.servicecb, 530, 460)
            self.fix.show_all()
            self.misServiceProvider = True
        else:
            self.misServiceProvider = False
            
    def selete_service(self, entry):
        self.mServiceName = self.servicelist.index(entry.get_text())+1

        