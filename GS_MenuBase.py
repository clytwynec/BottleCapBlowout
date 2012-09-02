import pygame
import sys
import os

from GameState import *
from GameKernel import *
import Colors

from pygame.locals import *

class GS_MenuBase(GameState):
	def __init__(self, name, kernel, gsm):
		GameState.__init__(self, name, kernel, gsm)

		self.mHeading = None
		self.mHeadingRect = None
		self.mMenuItems = {}
		self.mMenuImages = {}
		self.mMenuImagesHover = {}
		self.mMenuRects = {}

	def Initialize(self):

		return GameState.Initialize(self)

	def Destroy(self):
		return GameState.Destroy(self)

	def Pause(self):

		return GameState.Pause(self)

	def Unpause(self):

		return GameState.Unpause(self)

	def HandleEvent(self, event):
		if event.type == MOUSEMOTION:
			for item in self.mMenuRects:
				if (self.mMenuRects[item].collidepoint(event.pos) and item in self.mMenuImagesHover):
					self.mMenuItems[item] = self.mMenuImagesHover[item]
				else:
					self.mMenuItems[item] = self.mMenuImages[item]
		elif event.type == MOUSEBUTTONDOWN:
			for item in self.mMenuRects:
				if (self.mMenuRects[item].collidepoint(event.pos)):
					if (item == "Exit"):
						pygame.quit()
						sys.exit()
					else:
						self.mGameStateManager.SwitchState(item)


	def Update(self, delta):
		if (self.mHeading):
			self.mKernel.DisplaySurface().blit(self.mHeading, self.mHeadingRect)

		for item in self.mMenuItems:
			self.mKernel.DisplaySurface().blit(self.mMenuItems[item], self.mMenuRects[item])

		return GameState.Update(self, delta)