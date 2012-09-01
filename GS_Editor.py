import pygame
import os
import math

from GameState import *
from Level import *
from pygame.locals import *

class GS_Editor(GameState):
	def __init__(self, kernel, gsm, levelName):
		GameState.__init__(self, "Editor", kernel, gsm)

		self.mLevelName = levelName
		self.mLevel = Level(kernel)

	def Initialize(self):

		self.mLevel.LoadLevel(self.mLevelName)

		return GameState.Initialize(self)

	def Destroy(self):

		return GameState.Destroy(self)

	def Pause(self):

		return GameState.Pause(self)

	def Unpause(self):

		return GameState.Unpause(self)

	def HandleEvent(self, event):
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mLevel.Update(delta)

		self.mLevel.Draw()

		return GameState.Update(self, delta)