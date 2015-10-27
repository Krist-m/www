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
from signupui import *
from  screen import *
'''
Created on Jan 21, 2015

@author: kristapher
'''           
lock = None



class SigninUI:

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
        self.window.set_title("WWW")        
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

        self.mUsername = gtk.Entry(max=30)     
        self.mUsername.set_text("User Name")
        self.mPassWord = gtk.Entry(max=30)
        self.mPassWord.set_visibility(False)
        #self.mPassWord.connect("insert-at-cursor", self.password_edit_event)
        #self.mPassWord.set_text("Password")
                
        self.signup = gtk.Button()
        self.signup.set_label("Sign Up")
        self.signup.connect("clicked", self.signup_event, "New sign up")

        self.signin = gtk.Button()
        self.signin.set_label("Sign In")
        self.signin.connect("clicked", self.signin_event, "Log in")
        
        self.rememberPW = gtk.CheckButton("  Remember password")
        if os.path.exists(os.getcwd()+os.sep+"credentails"):
            self.rememberPW.set_active(True)
            f = open(os.getcwd()+os.sep+'credentails', 'rb')
            line = f.readline()
            f.close()
            line = line.split(":")
            self.mUsername.set_text(line[0])
            self.mPassWord.set_text(line[1])
            self.mIsRememberPasswordEnabled = True
        else:
            self.mIsRememberPasswordEnabled = False
            
        self.rememberPW.connect("toggled", self.remember_password, "RPW")  
          
        fix = gtk.Fixed()
        fix.put(borderimage, 10, 10)
        fix.put(image, 40, 25)
        fix.put(self.mUsername, 220, 40)
        fix.put(self.mPassWord, 220, 70)
        fix.put(self.signup, 219, 100)
        fix.put(self.signin, 325, 100)
        fix.put(self.rememberPW, 219, 130)
        
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
    
    def signup_event(self, widget, data=None):
        self.window.destroy()
        signup = SignupUI()
        signup.main()

    
    def signin_event(self, widget, data=None):
        res = self.__check_credentails()
        print res
        if res is not None:
            if self.mIsRememberPasswordEnabled:
                self.__store_password()
            self.window.destroy()
            import home
            home = home.HomeUI(User.create_from_list(res))
            home.main()
        else:
            print "Phone and Password not Matching"
            message = gtk.MessageDialog(type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK)
            message.set_markup("Phone number and Password did not match try to login again...")        
            message.run()
            message.destroy()
    
    def password_edit_event(self, widget, data=None):
        print "test"
        self.mPassWord.set_text("")
        self.mPassWord.set_visibility(False)
   
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()
        
    def __check_credentails(self):
        phoneno = self.mUsername.get_text()
        passwd = self.mPassWord.get_text()
        return DBAPI().check_for_autorization(phoneno, passwd)
        
    def remember_password(self, widget, data=None):
        if widget.get_active():
            self.mIsRememberPasswordEnabled = True
        else:
            self.mIsRememberPasswordEnabled = False  
            os.system("rm "+os.getcwd()+os.sep+"credentails")
      
    def __store_password(self):
        f = open(os.getcwd()+os.sep+'credentails', 'wb')
        f.write(self.mUsername.get_text()+":"+self.mPassWord.get_text())
        f.close()

    
      
    
    