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
		self.mLevel = Level(kernel, 650)

		self.mEntityBox = pygame.Rect(650, 0, 150, 600)

		self.mCurrentEntity = None
		self.mGhostEntity = None

		self.mSelectedEntity = None
		self.mEntitySelects = []
		self.mAvailableEntities = [
			"Bee",
			"Box",
			"RedCap",
			"BlueCap",
			"GoldCap",
			"Hive"
		]

		self.mSaveLevelImage, self.mSaveLevelRect = kernel.ImageManager().LoadImage("saveLevel.bmp", False)
		self.mSaveLevelRect.topleft = (725  - (self.mSaveLevelRect.width / 2), 570)
		
		self.mMainMenuImage, self.mMainMenuRect = kernel.ImageManager().LoadImage("mainmenu_ed.bmp", False)
		self.mMainMenuRect.topleft = (725  - (self.mSaveLevelRect.width / 2), 540)

		self.mGroundLevel = 570

		self.mScrollDirection = 0

		self.mFont = pygame.font.SysFont("Helvetica", 16, True)

	def Initialize(self):
		self.mLevel.LoadLevel(self.mLevelName)

		currentHeight = 10
		for i in range(len(self.mAvailableEntities)):
			module = __import__(self.mAvailableEntities[i])
			_EntityClass = getattr(module, self.mAvailableEntities[i])

			# Hacky passing in self.mKernel, but since it has Display surface, it works
			entity = _EntityClass(self.mKernel, self.mKernel)
			entity.SetPosition([ 725 - (entity.Rect().width / 2), currentHeight])

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

				if (self.mSaveLevelRect.collidepoint(event.pos)):
					self.mLevel.SaveLevel(self.mLevelName)

				elif (self.mMainMenuRect.collidepoint(event.pos)):
					self.mGameStateManager.SwitchState("MainMenu")

				else:
					for entity in self.mEntitySelects:
						if (entity.Rect().collidepoint(event.pos)):
							self.mSelectedEntity = entity

							classname = self.mSelectedEntity.__class__.__name__
							module = __import__(classname)
							_Entity = getattr(module, classname)

							self.mGhostEntity = _Entity(self.mKernel, self.mKernel)
							self.mGhostEntity.SetPosition(list(event.pos))
							return

					self.mGhostEntity = None
					self.mSelectedEntity = None
			else:
				if (self.mSelectedEntity):
					classname = self.mSelectedEntity.__class__.__name__
					module = __import__(classname)
					_Entity = getattr(module, classname)

					newEntity = _Entity(self.mKernel, self.mLevel)
					self.mLevel.AddEntity(newEntity, self.mLevel.ScreenToLevelCoordinates(event.pos))
					self.mLevel.CalcMaxScore()

				elif (self.mCurrentEntity):
					self.mCurrentEntity.SetPosition(list(self.mLevel.ScreenToLevelCoordinates(event.pos)))
					self.mCurrentEntity = None

				else:
					self.mGhostEntity = None
					self.mCurrentEntity = self.mLevel.EntityAt(event.pos)

		elif (event.type == MOUSEMOTION):
			if (self.mCurrentEntity and event.pos[0] < 576 and event.pos[0] > 0):
				self.mCurrentEntity.SetPosition(list(self.mLevel.ScreenToLevelCoordinates(event.pos)))

			elif (self.mSelectedEntity and event.pos[0] < 576 and event.pos[0] > 0):
				if (not self.mGhostEntity):
					classname = self.mSelectedEntity.__class__.__name__
					module = __import__(classname)
					_Entity = getattr(module, classname)

					self.mGhostEntity = _Entity(self.mKernel, self.mKernel)

				self.mGhostEntity.SetPosition(list(event.pos))

		elif (event.type == KEYDOWN):
			if (event.key == K_a):
				self.mScrollDirection = -4
			elif (event.key == K_d):
				self.mScrollDirection = 4
			elif (event.key == K_BACKSPACE and self.mCurrentEntity):
				self.mLevel.RemoveEntity(self.mCurrentEntity)
				self.mCurrentEntity = None
				self.mLevel.CalcMaxScore()

		elif (event.type == KEYUP):
			if (event.key == K_a or event.key == K_d):
				self.mScrollDirection = 0

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		# Don't animate things
		#self.mLevel.Update(delta)
		self.mLevel.Scroll(self.mScrollDirection)

		self.mLevel.Draw()

		if (self.mCurrentEntity):
			pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.GREEN, self.mCurrentEntity.Rect(), 2)

		self.mLevel.Blit()

		if (self.mGhostEntity):
			self.mGhostEntity.Draw()
			pygame.draw.rect(self.mKernel.DisplaySurface(), Colors.RED, self.mGhostEntity.Rect(), 2)

		pygame.draw.line(self.mKernel.DisplaySurface(), Colors.BLUE, (0, self.mGroundLevel), (800, self.mGroundLevel), 4)
		pygame.draw.line(self.mKernel.DisplaySurface(), Colors.RED, (self.mLevel.mLevelLength - 1500 - self.mLevel.mCameraX, 0), (self.mLevel.mLevelLength - 1500 - self.mLevel.mCameraX, 600), 4)

		pygame.draw.rect(self.mKernel.DisplaySurface(), Colors.LIGHT_GREY, self.mEntityBox)

		for entity in self.mEntitySelects:
			entity.Draw()

		if (self.mSelectedEntity):
			selectedRect = self.mSelectedEntity.Rect()
			pygame.draw.rect(self.mKernel.DisplaySurface(), Colors.RED, self.mSelectedEntity.Rect(), 2)

		self.mKernel.DisplaySurface().blit(self.mMainMenuImage, self.mMainMenuRect)
		self.mKernel.DisplaySurface().blit(self.mSaveLevelImage, self.mSaveLevelRect)

		textSurface = self.mFont.render("Max Score: " + str(self.mLevel.mMaxScore), True, Colors.WHITE)
		self.mKernel.DisplaySurface().blit(textSurface, (40, 580, textSurface.get_rect().width, textSurface.get_rect().height))

		return GameState.Update(self, delta)