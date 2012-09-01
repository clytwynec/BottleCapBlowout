from Entity import *
import pygame

class Person(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("playertest.bmp")

		self.mVelocity =  [0,1]

		self.mGravity = 1

		self.mGroundLevel = 0
		self.mScore = 0
		self.mJumpCount = 0

		self.mFrameRect = pygame.Rect(0, 0, 64, 64)
		self.mFrameWidth = 64
		self.mAnimationSpeed = 4

	def OnCollision(self, other):	
		if other.IsA('Collectable') or other.IsA('Obstacle'):
			self.UpdateScore(other.mValue)

		if other.IsA('Balloon'):
			self.UpdateScore(other.mValue)
			other.EmptyCoins()

		return

	def SetGroundLevel(self, groundLevel):
		self.mGroundLevel = groundLevel

	def UpdateScore(self, pointsVal):
		self.mScore += pointsVal
		return self.mScore


	def Update(self, delta):
		self.mVelocity[1] += self.mGravity 
		self.mPosition[1] += self.mVelocity[1] 

		if self.mPosition[1] > self.mGroundLevel - self.mRect.height:
			self.mPosition[1] = self.mGroundLevel - self.mRect.height
			self.mJumpCount = 0

			self.mVelocity[1] = 0
		Entity.Update(self, delta)  

	

