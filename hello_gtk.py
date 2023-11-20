#! /usr/bin/python3
# FROM: 
#  - https://www.gtk.org/docs/language-bindings/python/
#  - https://zetcode.com/python/gtk/
#  - https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html#example
#
# not yet release----

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

## each function should have a comment
def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    hbox = Gtk.HBox(spacing=6)
    vbox = Gtk.VBox(spacing=6)
    win.add(hbox)
    hbox.pack_start(vbox, True, True, 10)
    btn = Gtk.Button(label="Hello, World!")
    btn.connect('clicked', lambda x: win.close())
    btn2 = Gtk.Button(label="Everything")
    btn2.connect('clicked', lambda x: print("Nothing ", x))
    vbox.pack_start(btn, expand=True, fill=True, padding=10)
    vbox.pack_start(btn2, expand=True, fill=True, padding=10)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)

