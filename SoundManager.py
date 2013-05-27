import pygame
import os

from pygame.locals import *

class SoundManager:
	def __init__(self, kernel):
		self.mLoadedSounds = {}
		self.mKernel = kernel

	def LoadSound(self, filename):
		if (filename in self.mLoadedSounds):
			return self.mLoadedSounds[filename]
		else:
			sound = pygame.mixer.Sound(os.path.join("data", "sounds", filename))
			self.mLoadedSounds[filename] = sound
			return sound