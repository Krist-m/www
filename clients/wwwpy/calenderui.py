#!/usr/bin/env python


import pygtk
pygtk.require('2.0')
import gtk, pango
import time

class CalendarUI:
    DEF_PAD = 10
    DEF_PAD_SMALL = 5
    TM_YEAR_BASE = 1900


    def calendar_date_to_string(self):
        year, month, day = self.calwin.get_date()
        mytime = time.mktime((year, month+1, day, 0, 0, 0, 0, 0, -1))
        return time.strftime("%x", time.localtime(mytime))

    def calendar_day_selected(self, widget):
        date = self.calendar_date_to_string()
        self.cb_date_entry.set_text(date)
        print date
        self.window.destroy()

    def __init__(self, cb_date_entry):

        self.calwin = None
        self.cb_date_entry = cb_date_entry

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.set_title("Select date")
        self.window.connect("destroy", lambda x: gtk.main_quit())

        self.window.set_resizable(False)

        vbox = gtk.VBox(False, self.DEF_PAD)
        self.window.add(vbox)

        # The top part of the self.window, Calendar, flags and fontsel.
        hbox = gtk.HBox(False, self.DEF_PAD)
        vbox.pack_start(hbox, False, False, self.DEF_PAD)
        hbbox = gtk.HButtonBox()
        hbox.pack_start(hbbox, False, False, self.DEF_PAD)
        hbbox.set_layout(gtk.BUTTONBOX_SPREAD)

        # Calendar widget
        frame = gtk.Frame("Calendar")
        hbbox.pack_start(frame, False, True, self.DEF_PAD)
        calendar = gtk.Calendar()
        self.calwin = calendar               
        calendar.connect("day_selected", self.calendar_day_selected)

        #self.calendar_set_flags()
        frame.add(calendar)
        
        hbox2 = gtk.HBox(False)
        vbox.pack_start(hbox2)
        time =  gtk.Label()
        time.set_label("Time:")   
        hbox2.add(time)
        self.statecb = gtk.combo_box_entry_new_text()
        clist = [i for i in range(23)]
        for c in clist:
            self.statecb.append_text(str(c))
        self.statecb.child.connect('changed', self.time_select)
        self.statecb.set_active(0)
        hbox2.add(self.statecb)
        hbox.show()

       
        self.window.show_all()
        
    def time_select(self, entry):
        #self.cb_date_entry = self.cb_date_entry.get_text() + ":" + entry
        pass

    def main(self):
        date = self.calendar_date_to_string()
        self.cb_date_entry.set_text(date)
        gtk.main()
        return 0