import os, sys
import settings
import Image, ImageEnhance, ImageDraw, ImageFont
from PIL.ExifTags import TAGS

class Watermark(object):
	
	def __init__(self, im):
		self.im = im
		self.color = settings.CONFIG["watermark"]["color"]
		self.background_color = settings.CONFIG["watermark"]["background_color"]
		self.text = settings.CONFIG["watermark"]["text"]
		self.font_size = settings.CONFIG["watermark"]["font_size"]
		self.margin = settings.CONFIG["watermark"]["margin"]
		self.text_opacity = settings.CONFIG["watermark"]["text_opacity"]
		self.background_opacity = settings.CONFIG["watermark"]["background_opacity"]
		font_path = os.path.join(settings.FONTS_ROOT, settings.CONFIG["watermark"]["font"])
		self.font = ImageFont.truetype(font_path, self.font_size)
		
	def render(self):
		if self.im.mode != "RGBA":
			self.im = self.im.convert("RGBA")
			
		margin = (self.margin,self.margin)
		self.im = self.put_substrate(self.im, self.background_color, self.background_opacity)
		self.im = self.imprint(self.im, self.text, self.font, self.color, self.text_opacity, margin)
		
		return self.im

	def imprint(self, im, inputtext, font=None, color=None, opacity=.6, margin=(30,30)):
		"""
		imprints a PIL image with the indicated text in lower-right corner
		"""
		if im.mode != "RGBA":
			im = im.convert("RGBA")
		textlayer = Image.new("RGBA", im.size, (0,0,0,0))
		textdraw = ImageDraw.Draw(textlayer)
		textsize = textdraw.textsize(inputtext, font=font)
		textpos = [im.size[i]-textsize[i]-margin[i] for i in [0,1]]
		textdraw.text(textpos, inputtext, font=font, fill=color)
		if opacity != 1:
			textlayer = self.reduce_opacity(textlayer,opacity)
		return Image.composite(textlayer, im, textlayer)
		
	def put_substrate(self, im, background_color, opacity):
		"""
		Draws opaque rectangle on a PIL image in a lower-right corner
		"""

		background_layer = Image.new("RGBA", im.size, (0,0,0,0))
		background_draw = ImageDraw.Draw(background_layer)
		
		
		text_length_multiplier = 0.5
		text_height_multiplier = 1.2
		text_box_height = int(self.font_size*text_height_multiplier + self.margin*2)
		text_box_width = int(len(self.text)*self.font_size*text_length_multiplier + self.margin*2)
		print text_box_width
		
		background_draw.rectangle((im.size[0]-text_box_width, im.size[1]-text_box_height, im.size[0], im.size[1]), fill=background_color, outline="#333333")
		
		if opacity != 1:
			background_layer = self.reduce_opacity(background_layer, opacity)
		return Image.composite(background_layer, im, background_layer)
		

	def reduce_opacity(self, im, opacity):
		"""Returns an image with reduced opacity."""
		assert opacity >= 0 and opacity <= 1
		if im.mode != 'RGBA':
			im = im.convert('RGBA')
		else:
			im = im.copy()
		alpha = im.split()[3]
		alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
		im.putalpha(alpha)
		return im


	  # def put_watermark_background
	  #   pointsize = 11
	  #   background_length = @watermark_text.size*pointsize*0.95
	  # 
	  #   background = Magick::Draw.new
	  #   background.fill("black")
	  #   background.fill_opacity(0.6)
	  #   background.rectangle(@desired_width-background_length, @desired_height-30, @desired_width, @desired_height)
	  #   background.draw(@file)
