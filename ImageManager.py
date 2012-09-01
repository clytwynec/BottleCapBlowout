import pygame
import os
import Colors

class ImageManager:
	def __init__(self):
		self.mLoadedImages = {}

	def LoadImage(self, filename):
		if (filename in self.mLoadedImages):
			return self.mLoadedImages[filename], self.mLoadedImages[filename].get_rect()
		else:
			image = pygame.image.load(os.path.join("data", "images", filename)).convert()
			image.set_colorkey(Colors.TRANSPARENT);
			self.mLoadedImages[filename] = image
			return image, image.get_rect()