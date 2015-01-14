#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import os.path

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def tempFiles(dir):
  filenames = os.listdir(dir)
    # print 'filenames' , filenames

    # cmd = 'ls ' + dir + '|grep "__"'
    # print 'cmd is ',cmd
  abspath = os.path.abspath(dir)
    # print abspath
  files=[]
  for file in filenames:
    if '__' in file: 
       files.append(abspath + '/'+ file)
 
  return files
   
def copytodir(copytodir,srcpath):
  print 'copytodir ...'
  abspath = os.path.abspath(copytodir)
  abspathsrc = os.path.abspath(srcpath)
  cmd = 'mkdir ' + abspath
  (status,output) = commands.getstatusoutput(cmd)
  # check status for error 
  # if status !=0:
  #   print 'status error',output
  #   sys.exit(1) 
  cmd = 'cp ' + ' '.join(tempFiles(srcpath)) + ' '+ abspath 
  # print cmd
  (status,output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
   

def ziptodir(zipfilename,srcpath):
  print 'zip to file...'
  cmd = 'zip -j ' + zipfilename + ' ' + ' '.join(tempFiles(srcpath))
  # print cmd
  (status,output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
   

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:1]
    

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:1]
   


  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  else:  
   
    # if no --zip or dir 
    if todir:
      print 'copy to dir'
      copytodir(args[0],args[1] )
    elif tozip:
      print 'zip to file'
      ziptodir(args[0],args[1])
    else:
      print 'no dir no zip enter, just display path and files' 
      
      allfiles = tempFiles(args[0])
      print '\n'.join(allfiles)

  # +++your code here+++
  # Call your functions

if __name__ == "__main__":
  main()


