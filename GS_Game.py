import pygame
import os
import math
from Person import *
from Balloon import *
from GameState import *
from Level import *
from pygame.locals import *
import Colors

class GS_Game(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "Game", kernel, gsm)

		self.mLevelName = ""
		self.mLevel = None

		self.mGroundLevel = 570

		self.mHighScores = {}

		self.mScrollSpeed = 2
		self.mLives = 3

		self.mPaused = 0

	def Initialize(self):
		self.mLevelName = "Level1.lvl"
		self.mLevel = Level(self.mKernel, 800)

		self.mLevel.LoadLevel(self.mLevelName)
		self.mLevel.mScrollSpeed = self.mScrollSpeed

		self.mCordImage, self.mCordRect = self.mKernel.ImageManager().LoadImage("cord.bmp")
		self.mCordRect.bottomleft = (0, self.mGroundLevel)

		self.mPerson = Person(self.mKernel, self.mLevel)
		self.mPerson.SetPosition([128, self.mGroundLevel])
		self.mPerson.mScreenOffset = 128
		self.mPerson.SetGroundLevel(self.mGroundLevel)

		self.SpawnBalloon()

		return GameState.Initialize(self)

	def SpawnBalloon(self):
		self.mBalloon = Balloon(self.mKernel, self.mLevel)
		self.mBalloon.SetPosition([ self.mPerson.Rect().right, self.mGroundLevel - self.mBalloon.Rect().height - 128 ])
		self.mBalloon.mGroundLevel = 500

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
		elif (event.type == KEYDOWN):
			if (event.key == K_UP):
				self.mPerson.Jump()
			elif (event.key == K_DOWN):
				self.mPerson.Duck()
			elif (event.key == K_SPACE):
				self.mBalloon.mBlown = 1
			elif (event.key == K_p):
				self.mPaused = (self.mPaused + 1) % 2
			elif (event.key == K_ESCAPE):	
				self.mGameStateManager.SwitchState('MainMenu')

		elif(event.type == KEYUP):
			if (event.key == K_SPACE):
				self.mBalloon.mBlown = 0  
			elif (event.key == K_DOWN):
				self.mPerson.Run()

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		if self.mPaused == 0:
			self.mLevel.Scroll(self.mScrollSpeed)
			self.mLevel.Update(delta)

			self.mPerson.Update(delta)
			self.mBalloon.Update(delta)

			self.mLevel.CheckCollisions(self.mPerson)
			self.mLevel.CheckCollisions(self.mBalloon)

			if (self.mPerson.CheckCollision(self.mBalloon) and self.mBalloon.CheckCollision(self.mPerson)):
				self.mPerson.OnCollision(self.mBalloon)
				self.mBalloon.OnCollision(self.mPerson)
					
			if (self.mBalloon.mPopped and self.mBalloon.mPosition[0] < self.mLevel.mCameraX and self.mLives > 0):
				self.SpawnBalloon()
			
		self.mLevel.Draw()
	
		# for entity in self.mLevel.mEntities:
		# 	pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.BLUE, entity.Rect(), 2)

		# 	if (entity.mCollisionRect):
		# 		pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.RED, entity.mCollisionRect, 2)

		self.mCordRect.bottomright = self.mPerson.Rect().bottomleft
		self.mLevel.DisplaySurface().blit(self.mCordImage, self.mCordRect)

		self.mPerson.Draw()
		#pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.BLUE, self.mPerson.Rect(), 2)
		#pygame.draw.rect(self.mLevel.DisplaySurface(), Colors.RED, self.mPerson.mCollisionRect, 2)
		self.mBalloon.Draw()

		self.mLevel.Blit()


		return GameState.Update(self, delta)

	def SaveScore(self):
		if self.mLevelName in self.mHighScores:
			if self.mPerson.mScore > self.mHighScores[self.mLevelName]:
				self.mHighScores[self.mLevelName] = self.mPerson.mScore
		else:
			self.mHighScores.append[self.mLevelName : self.mPerson.mScore]
