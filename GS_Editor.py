import pygame
import os
import math

from GameState import *
from Level import *
from pygame.locals import *

class GS_Editor(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "Editor", kernel, gsm)

	def Initialize(self):

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
		
		return GameState.Update(self, delta)