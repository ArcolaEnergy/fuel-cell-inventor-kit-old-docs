#!/usr/bin/python
import sys
import re


filename = sys.argv[1]
try:
  fd = open(filename)
  lines = fd.readlines()
  r_image = re.compile( "(.*<imageobject)>(.*?)pics/(.*?)(</imageobject>.*)")
  for line in lines:
    r = r_image.match(line)
    if r:
      print "%s%s%s%s%s%s" % ( r.group(1), ' role="fo">', r.group(2), "pics/fo/", r.group(3), r.group(4) )
      print "%s%s%s%s%s%s" % ( r.group(1), ' role="html">', r.group(2), "pics/html/", r.group(3), r.group(4) )
    else:
      print line,
except:
  print "bad file", filename
  exit(1)


