#!/usr/bin/python
# -*- coding: utf-8 -*-
import dbus
import avahi
import gobject 
import dbus.glib

bus = dbus.SystemBus()
server = dbus.Interface(bus.get_object(avahi.DBUS_NAME, avahi.DBUS_PATH_SERVER), avahi.DBUS_INTERFACE_SERVER)
f = open('servers', 'w+')
f.close()

def new_service(interface, protocol, name, type, domain, flags):
   interface, protocol, name, type, domain, host, aprotocol, address, port, txt, flags = server.ResolveService(interface, protocol, name, type, domain, avahi.PROTO_UNSPEC, dbus.UInt32(0))
   try :
      f = open('servers', 'a')
      f.write("%s|%s:%s\n" % (name, address, port))
   finally :
      f.close()

stype = '_daap._tcp'
domain = 'local'
browser = dbus.Interface(bus.get_object(avahi.DBUS_NAME, server.ServiceBrowserNew(avahi.IF_UNSPEC, avahi.PROTO_UNSPEC, stype, domain, dbus.UInt32(0))), avahi.DBUS_INTERFACE_SERVICE_BROWSER)

browser.connect_to_signal('ItemNew', new_service)
try :
    gobject.MainLoop().run()
finally :
    pass
