import os
import sys

import settings
from lib.file import PhotoFile
from lib.directory import PhotoDirectory


#PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'photolib'))
#sys.path.insert(0, os.path.join(PROJECT_ROOT, 'compat'))

#sys.path.append(os.path.join(settings.SOURCE_ROOT, "IMG_8449.jpg"))
#outfile = os.path.splitext(infile)[0] + ".thumbnail"

infile = os.path.join(settings.SOURCE_ROOT, "IMG_8449.jpg")
photo = PhotoFile(infile)
#photo.resize()

directory = PhotoDirectory(settings.SOURCE_ROOT)
directory.process()
