import pygtk
from pango import DESCENT
pygtk.require('2.0')
import gtk
import pango
 
'''
__init__
do_print
print_text
format_text
===========
__init__
do_print
area_expose_cb
draw_text
format_text
area_expose_cb
draw_text
format_text

'''
 
class OrderPrint:
    def __init__(self):
        print "__init__"
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Drawing Area Example")
        window.connect("destroy", lambda w: gtk.main_quit())
        self.area = gtk.DrawingArea()
        self.area.set_size_request(400, 300)
        window.add(self.area)
 
        self.area.connect("expose-event", self.area_expose_cb)
        self.area.show()
        window.show()
        self.do_print()
 
    def area_expose_cb(self, area, event):
        print "area_expose_cb"
        self.style = self.area.get_style()
        self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
        self.draw_text()
        return True
 
    def do_print(self):
        print "do_print"
        print_op = gtk.PrintOperation()
        print_op.set_n_pages(1)
        print_op.connect("draw_page", self.print_text)
        res = print_op.run(gtk.PRINT_OPERATION_ACTION_PRINT_DIALOG, None)
 
    def draw_text(self):
        print "draw_text"
        self.pangolayout = self.area.create_pango_layout("")
        self.format_text()
        self.area.window.draw_layout(self.gc, 10, 10, self.pangolayout)
        return
 
    def print_text(self, operation=None, context=None, page_nr=None):
        print "print_text"
        self.pangolayout = context.create_pango_layout()
        self.format_text()
        cairo_context = context.get_cairo_context()
        cairo_context.show_layout(self.pangolayout)
        return
 
    def format_text(self):
        print "format_text"
        self.pangolayout.set_text("Name    :  John junior II\n Phono   :  9877654432\nAddress :  12 Oak Tree,\nEdison, \n New Jersey\nService :  pills")

    def draw_page(self, operation=None, context=None, page_nr=None, user_data=None):
        HEADER_HEIGHT = 1500
        
        cr = context.get_cairo_context()
        width = context.get_width()
        cr.rectangle(0, 0, width, HEADER_HEIGHT)
        
        cr.set_source_rgb(0.8, 0.8, 0.8)
        cr.fill()
        
        layout = context.create_pango_layout()
        
        desc = pango.FontDescription("sans 14")
    
        layout.set_font_description(desc)
        
        layout.set_text("some text")
        layout.set_width(int(width))
        layout.set_alignment(pango.ALIGN_CENTER)
        
        x, layout_height = layout.get_size()
        text_height = layout_height/pango.SCALE
        
        cr.move_to(width/2, (HEADER_HEIGHT - text_height)/2)
        cr.show_layout(layout)




