import pygame
import os
import math

from GS_Game import *

from Level import *
from pygame.locals import *

import Colors

class GS_Tutorial(GS_Game):
	def __init__(self, kernel, gsm):
		GS_Game.__init__(self, kernel, gsm)
		self.mName = "Tutorial"

		self.mScrollSpeed = 1

		self.mTutorialText = [ None ] * 5
		self.mTutorialRect = [ None ] * 5
		self.mTutorialStarts = [ (0, 400), (400, 1200), (1400, 2200), (2000, 2900), (3000, 3900) ]
		self.mCurrentText = 0

		self.mTutorialText[0], self.mTutorialRect[0] = self.mKernel.ImageManager().LoadImage("tutorial1.bmp")
		self.mTutorialText[1], self.mTutorialRect[1] = self.mKernel.ImageManager().LoadImage("tutorial2.bmp")
		self.mTutorialText[2], self.mTutorialRect[2] = self.mKernel.ImageManager().LoadImage("tutorial3.bmp")
		self.mTutorialText[3], self.mTutorialRect[3] = self.mKernel.ImageManager().LoadImage("tutorial4.bmp")
		self.mTutorialText[4], self.mTutorialRect[4] = self.mKernel.ImageManager().LoadImage("tutorial5.bmp")

	def Initialize(self):
		GS_Game.Initialize(self, "Tutorial")

	def Pause(self):
		self.Destroy()

	def Update(self, delta):
		GS_Game.Update(self, delta)

		for i in range(len(self.mTutorialText)):
			if (self.mLevel.mCameraX >= self.mTutorialStarts[i][0]):
				rect = pygame.Rect(self.mTutorialStarts[i][1] - self.mLevel.mCameraX, 150, self.mTutorialRect[i].width, self.mTutorialRect[i].height)
				self.mKernel.DisplaySurface().blit(self.mTutorialText[i], rect)
