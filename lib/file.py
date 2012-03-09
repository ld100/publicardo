import os, sys
import settings
import Image, ImageEnhance, ImageDraw, ImageFont
from PIL.ExifTags import TAGS
from subprocess import call
import watermark

class PhotoFile(object):
	
	size = settings.CONFIG["resize"]["wide_side_length"], settings.CONFIG["resize"]["wide_side_length"]
	
	def __init__(self, infile):
		self.infile = infile
		
	def resize(self):
		new_file_name = "_" + os.path.basename(self.infile)
		self.outfile = os.path.join(settings.DESTINATION_ROOT, new_file_name)
		if self.infile != self.outfile:
			try:
				im = Image.open(self.infile)
				im.thumbnail(self.size, Image.ANTIALIAS)
				im = self.put_watermark(im)
				im.save(self.outfile, "JPEG")
			except IOError:
				print "cannot create thumbnail for '%s'" % self.infile


	def put_watermark(self, im ):
		mark = watermark.Watermark(im)
		return mark.render()
		

	def put_exif(self):
		jhead_string = settings.JHEAD_BIN + " -q -te " + self.infile + " " + self.outfile
		return_code = os.system(jhead_string)
		#return_code = call(jhead_string, shell=True)
		
		
	def get_exif(self):
		ret = {}
		i = Image.open(self.infile)
		info = i._getexif()
		for tag, value in info.items():
			decoded = TAGS.get(tag, tag)
			ret[decoded] = value
		return ret		
		
	def process(self):
		self.resize()
		#self.put_watermark()
		self.put_exif()

	