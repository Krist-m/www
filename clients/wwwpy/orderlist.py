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
columns = ["      Order No.     ",
           "      Service       ",
           "      Date          ",
           "      Status        ",
           "      Comments       "]

sample = [["1234234", "Mineral water", "10/26/15", "In Progress", ""],
             ["3214344", "Maid",          "10/21/15", "Delivered", ""],
             ["3245234", "Truck",         "10/20/15", "Delivered", ""],
             ["3214344", "Maid",          "10/21/15", "Canceled", ""],
             ["3245234", "Truck",         "10/20/15", "Delivered", ""],
             ["6345233", "Minaral water", "10/18/15", "Service not available", ""],
             ["3214344", "Maid",          "10/21/15", "Canceled", ""],
             ["3245234", "Truck",         "10/20/15", "Delivered", ""],
             ["6345233", "Minaral water", "10/18/15", "Delivered", ""]]



class OrderList:

    def __init__(self):

        # the data in the model (three strings for each row, one for each
        # column)
        listmodel = gtk.ListStore(str, str, str, str, str)
        # append the values in the model
        for i in range(len(sample)):
            listmodel.append(sample[i])

        # a treeview to see the data stored in the model
        
        self.view = gtk.TreeView(model=listmodel)
        #self.view.set_size_request(600, 300)
        # for each column
        for i in range(len(columns)):
            # cellrenderer to render the text
            cell = gtk.CellRendererText()
            cell.set_property("xalign", 0.5)
            # the text in the first column should be in boldface
            #cell.set_property('size', 10)
            cell.set_property('background', 'light blue')
            # the column is created
            col = gtk.TreeViewColumn(columns[i], cell, text=i)
            col.set_spacing(100)
            #col.add_attribute(cell, "cell-background", 1)
            # and it is appended to the treeview
            self.view.append_column(col)

        # when a row is selected, it emits a signal
        self.view.get_selection().connect("changed", self.on_changed)

        # the label we use to show the selection
        self.label = gtk.Label()
        self.label.set_text("")
        
    def get_view(self):
        return self.view


    def on_changed(self, selection):
        # get the model and the iterator that points at the data in the model
        (model, iter) = selection.get_selected()
        # set the label to a new value depending on the selection
        self.label.set_text("\n %s %s %s" %
                            (model[iter][0],  model[iter][1], model[iter][2]))
        return True