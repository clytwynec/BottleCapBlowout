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

		self.mLevelName = "Level1.lvl"
		self.mLevel = Level(kernel, 800)

		self.mGroundLevel = 570


	def Initialize(self):
		self.mLevel.LoadLevel(self.mLevelName)

		self.mPerson = Person(self.mKernel, self.mLevel)
		self.mPerson.SetPosition([0, self.mGroundLevel])
		self.mPerson.SetGroundLevel(self.mGroundLevel)

		self.mBalloon = Balloon(self.mKernel, self.mLevel)
		self.mBalloon.SetPosition([400, 0])
		self.mBalloon.mGroundLevel = 500

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
		elif (event.type == KEYDOWN):
			if (event.key == K_UP):
				self.mPerson.Jump()
			elif (event.key == K_DOWN):
				self.mPerson.Duck()
			elif (event.key == K_SPACE):
				self.mBalloon.mBlown = 1

		elif(event.type == KEYUP):
			if (event.key == K_SPACE):
				self.mBalloon.mBlown = 0  
			elif (event.key == K_DOWN):
				self.mPerson.Run()

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		self.mLevel.Scroll(1)
		self.mLevel.Update(delta)

		self.mLevel.CheckCollisions(self.mPerson)

		self.mPerson.Update(delta)
		self.mBalloon.Update(delta)

		self.mLevel.Draw()
		self.mPerson.Draw()
		self.mBalloon.Draw()
		self.mLevel.Blit()
		return GameState.Update(self, delta)