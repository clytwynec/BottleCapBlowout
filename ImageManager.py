import pygame
import os
import Colors

from pygame.locals import *

class ImageManager:
	def __init__(self, kernel):
		self.mLoadedImages = {}
		self.mKernel = kernel

	def LoadImage(self, filename, transparent = True):
		if (filename in self.mLoadedImages):
			print filename
			return self.mLoadedImages[filename], self.mLoadedImages[filename].get_rect()
		else:
			image = pygame.image.load(os.path.join("data", "images", filename))
			image = image.convert(self.mKernel.DisplaySurface())

			if (transparent):
				image.set_colorkey(Colors.TRANSPARENT);
				image.set_alpha(255, RLEACCEL)
			
			self.mLoadedImages[filename] = image
			return image, image.get_rect()