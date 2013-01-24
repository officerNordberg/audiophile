#!/usr/bin/python
from daap import DAAPClient
import sys

class ItShell():
    session = None

    def do_connect(self, spec):
        if len(spec) == 0:
            server = "localhost"
            port = 3689
        elif spec.count(" ") == 0:
            server = spec
            port = 3689
        elif spec.count(" ") == 1:
            (server, port) = spec.split(" ")
        else:
            return

        client = DAAPClient()
        client.connect(server, port)
        self.session = client.login()
        self.do_database( self.session.library().id )

    def do_database(self, id):
        if not self.session:
            return
        databases = self.session.databases()
        for d in databases:
            if str(d.id) == str(id):
                self.database = d
                return

    def do_playlists(self):
        if not self.database:
            return
        playlists = self.database.playlists()
        for p in playlists:
            print "%s: %s"%(p.id, repr(p.name))
    
try:
    #import logging
    #logging.basicConfig(level=logging.DEBUG,
    #        format='%(asctime)s %(levelname)s %(message)s')
    # run the shell
    shell = ItShell()
    shell.do_connect(sys.argv[1])
    shell.do_playlists()
finally:
    if shell and shell.session:
        shell.session.logout()
