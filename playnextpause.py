#!/usr/bin/python
# Licensed under the MIT license
# http://opensource.org/licenses/mit-license.php

# Copyright 2009 - Jörgen Modin

""" play-next-pause is a simple remote control.

    Based on the Coherence UPnP/DLNA framework
    http://coherence.beebits.net
    
    Specifically the UPnP Inspector by Frank Scholz
"""

from twisted.internet import gtk2reactor
gtk2reactor.install()
from coherence.base import Coherence
from twisted.internet import reactor
import pygtk
pygtk.require("2.0")
import gtk

devices = {}
coherence = Coherence()

def device_found(device=None):
    #print "Found device %s \n%s \n%s \n%s" % (device.get_friendly_name(), device.get_usn(), device.get_device_type().split(':')[3].lower(), device.get_device_type())
    
    device_usn = device.get_usn()
    devices[device_usn] = {'friendly_name':device.get_friendly_name()}
    
    for service in device.services:
        _,_,_,service_class,version = service.service_type.split(':')
        if service_class not in ['AVTransport']:
            continue
        service.subscribe()
        
        for action in service.get_actions().values():
            if action.name in ('Stop', 'Pause', 'Previous','Next'):
                print "We have got action %s" % action.name
                devices[device_usn][action.name] = (action.call,{'InstanceID':0})
            elif action.name == 'Play':
                devices[device_usn][action.name] = (action.call,{'InstanceID':0,'Speed':1})
            elif action.name =='GetMediaInfo_Ext':
                pass
        make_remote_control_window(usn=device_usn)

def device_removed(usn=None):
    print "lost device %s" % usn

def execute_action(button, function, params):
    function(**params)
    
def make_remote_control_window(usn):
    if not devices.has_key(usn):
        return
    device = devices[usn]
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_default_size(300,33)
    window.set_title('%s' % device['friendly_name'])
    hbox = gtk.HBox(homogeneous=False, spacing=2)
    
    for action in ('Play','Stop', 'Pause', 'Previous','Next'):
        if device.has_key(action):            
            button = gtk.Button(action)
            function, params = device[action]
            button.connect('clicked',execute_action, function ,params)
            hbox.pack_start(button)
            
    window.add(hbox)
    window.show_all()

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.connect("delete_event", lambda x,y: reactor.stop())
window.set_default_size(100,33)
window.set_title('DLNA Remote control')
button = gtk.Button('Quit remote control')
button.connect("clicked", lambda x: reactor.stop())
hbox = gtk.HBox(homogeneous=False, spacing=10)
hbox.pack_start(button,False,False,2)
hbox.pack_end(button,False,False,20)
window.add(hbox)
window.show_all()

coherence.connect(device_found, 'Coherence.UPnP.RootDevice.detection_completed')
coherence.connect(device_removed, 'Coherence.UPnP.RootDevice.removed')

reactor.run()

