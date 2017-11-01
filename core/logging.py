#!/usr/bin/python
import time, os, sys

import logging
RescoursesDir = os.getcwd()

dandtime = time.strftime("%H:%M:%S")

logfile = "%s/storage/logs/%s.log" % (RescoursesDir,dandtime)

class Tee(object):
  def __init__(self):
    self.file = open(logfile, 'a')
    self.stdout = sys.stdout

  def __del__(self):
    sys.stdout = self.stdout
    self.file.close()

  def write(self, data):
    self.file.write(data)
    self.stdout.write(data)

sys.stdout = Tee()
