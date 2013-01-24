#!/usr/bin/python
from daap import DAAPClient
import sys

class Playlist():

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

        print "No such database"

    def do_playlist(self, id):
        """
        playlist <id> - use a particular playlist
        """
        if not self.session:
            return
        if not self.database:
            return
        playlists = self.database.playlists()
        for p in playlists:
            if str(p.id) == str(id):
                self.database = p
                self._tracks = p.tracks()
                return


    def get_tracks(self, reset = 0):
        if reset or "_tracks" not in self.__dict__:
            self._tracks = self.database.tracks()
        return self._tracks


    def do_tracks(self, other):
        """tracks - list tracks in the selected database"""
        if not self.database:
            print "No current database"
            return
        tracks = self.get_tracks()
# [DAAPTrack(self.database, t) for t in track_list]
        return map(self.do_url, tracks)

    def do_urls(self, track):
        return "http://%s:%s/databases/%s/items/%s.%s?session-id=%s"%(track.database.session.connection.hostname, 
                                                                      track.database.session.connection.port, 
																	  track.database.id, 
																	  track.id, 
																	  track.type, 
																	  track.database.session.sessionid)

try:
    import logging
    logging.basicConfig(level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s')
    # run the shell
    shell = ItShell()
    shell.do_connect(sys.argv[1])
    shell.do_playlist(sys.argv[2])
    print
finally:
    if shell and shell.session:
        shell.session.logout()
