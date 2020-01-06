# Load external packages
import time
import os
import sys

class measure_time:
    def __init__(self):
        if sys.platform == 'win32':
            # On Windows, the best timer is time.clock
            self.default_timer = time.clock
        else:
            # On most other platforms the best timer is time.time
            self.default_timer = time.time
    
    def start(self):
        self.ini = self.default_timer()
    
    def end(self, pages):
        print("Editor processed " + str(pages) + " pages in " + str(self.default_timer() - self.ini) + " seconds" )