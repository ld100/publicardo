import os, sys
import settings
import imghdr
from file import PhotoFile

class PhotoDirectory(object):
	
	_images_list = []
	
	def __init__(self, directory):
		self.directory = directory
		
	def images(self):
		images_list = []
		listing = os.listdir(self.directory)
		for file_name in listing:
			file_path = os.path.join(self.directory, file_name)
			if os.path.isfile(file_path) and "jpeg" == imghdr.what(file_path):
				#print file_path
				images_list.append(file_path)
		self._images_list = images_list
		return images_list

	def process(self):
		for file_path in self.images():
			photo = PhotoFile(file_path)
			photo.process()
	
