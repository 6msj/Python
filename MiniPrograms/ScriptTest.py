import os

location = raw_input("Where is the file?")
os.system('rsync %r /home/jamesarch/Desktop') % location
