#!/usr/bin/python
import unittest
from playlist import Playlist
from daap import DAAPTrack

class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.shell = Playlist()


#    def test_shuffle(self):
 #       self.assertEqual(self.seq, range(10))

#        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_do_url(self):
        track = DAAPTrack()
        self.shell.do_url(track)
        self.assertTrue(element in self.seq)

 #   def test_sample(self):
  #      with self.assertRaises(ValueError):
   #         random.sample(self.seq, 20)
    #    for element in random.sample(self.seq, 5):
     #       self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
