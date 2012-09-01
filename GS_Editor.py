import pygame
import os
import math

from GameState import *
from Level import *
from pygame.locals import *
import Colors

class GS_Editor(GameState):
	def __init__(self, kernel, gsm, levelName):
		GameState.__init__(self, "Editor", kernel, gsm)

		self.mLevelName = levelName
		self.mLevel = Level(kernel)

		self.mEntityBox = pygame.Rect(800, 0, 224, 768)

		self.mSelectedEntity = None
		self.mEntitySelects = []
		self.mAvailableEntities = [
			"Bee",
			"Box",
			"BottleCap",
		]

	def Initialize(self):
		self.mLevel.LoadLevel(self.mLevelName)

		currentHeight = 10
		for i in range(len(self.mAvailableEntities)):
			module = __import__(self.mAvailableEntities[i])
			_EntityClass = getattr(module, self.mAvailableEntities[i])

			entity = _EntityClass(self.mKernel)
			entity.SetPosition([ 912 - (entity.Rect().width / 2), currentHeight])

			currentHeight += entity.Rect().height + 10

			self.mEntitySelects.append(entity)

		return GameState.Initialize(self)

	def Destroy(self):

		return GameState.Destroy(self)

	def Pause(self):

		return GameState.Pause(self)

	def Unpause(self):

		return GameState.Unpause(self)

	def HandleEvent(self, event):
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()
		elif (event.type == MOUSEBUTTONDOWN):
			if (self.mEntityBox.collidepoint(event.pos)):
				for entity in self.mEntitySelects:
					if (entity.Rect().collidepoint(event.pos)):
						self.mSelectedEntity = entity
						break
			else:
				if (self.mSelectedEntity):
					classname = self.mSelectedEntity.__class__.__name__
					module = __import__(classname)
					_Entity = getattr(module, classname)

					newEntity = _Entity(self.mKernel)
					self.mLevel.AddEntity(newEntity, list(event.pos))

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mLevel.Update(delta)

		self.mLevel.Draw()

		pygame.draw.rect(self.mKernel.DisplaySurface(), Colors.LIGHT_GREY, self.mEntityBox)

		for entity in self.mEntitySelects:
			entity.Draw()

		if (self.mSelectedEntity):
			pygame.draw.rect(self.mKernel.DisplaySurface(), Colors.RED, self.mSelectedEntity.Rect(), 2)

		return GameState.Update(self, delta)