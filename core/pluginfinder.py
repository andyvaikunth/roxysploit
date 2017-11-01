import os
import readline
import glob
import sys
from subprocess import check_output

os.system("ls plugins/*.plugin > storage/plugins.loaded")
x = open("storage/plugins.loaded", "r")

#ripas = os.path.splitext(content)[-2]
#datasw = ripas.split('/')[1]

