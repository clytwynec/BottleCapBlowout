from Entity import *
import pygame

class Person(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mRunImage, self.mRunRect = self.mKernel.ImageManager().LoadImage("player_run128.bmp")
		self.mDuckImage, self.mDuckRect = self.mKernel.ImageManager().LoadImage("player_duck.bmp")
		self.mJumpImage1, self.mJumpRect1 = self.mKernel.ImageManager().LoadImage("player_jump1.bmp")
		self.mJumpImage2, self.mJumpRect2 = self.mKernel.ImageManager().LoadImage("player_jump2.bmp")

		self.mImage = self.mRunImage
		self.mRect = pygame.Rect(0, 0, 128, 128)
		self.mCollisionRect = pygame.Rect(0, 0, 60, 115)

		self.mVelocity =  [0,1]

		self.mGravity = 1

		self.mGroundLevel = 0
		self.mScore = 0
		self.mJumpCount = 0
		self.mPause = 0

		self.mFrameRect = pygame.Rect(0, 0, 128, 128)
		self.mFrameWidth = 128
		self.mAnimationSpeed = 4

	def OnCollision(self, other):
		if other.IsA('Collectable'):
			self.UpdateScore(other.mValue)
		elif other.IsA('Obstacle'):
			self.UpdateScore(other.mValue)


		if other.IsA('Obstacle'):
			self.UpdateScore(other.mValue)

			if (other.mSolid):
				#Moving down
				print self.mCollisionRect.bottom, other.Rect().top
				if (self.mVelocity[1] >= 0 and self.mCollisionRect.bottom - other.Rect().top <= 10):
					if (self.mJumpCount > 0):
						self.mJumpCount = 0
						self.Run()

					self.mVelocity[1] = 0
					self.mGravity = 0

		if other.IsA('Balloon'):
			self.UpdateScore(other.mValue)

		return

	def SetGroundLevel(self, groundLevel):
		self.mGroundLevel = groundLevel

	def UpdateScore(self, pointsVal):
		self.mScore += pointsVal

		return self.mScore

	def Jump(self):
		self.mJumpCount +=1
		if self.mJumpCount <= 2:
			self.mVelocity[1] = -15

		if (self.mJumpCount == 1):
			self.mImage = self.mJumpImage1
		else:
			self.mImage = self.mJumpImage2

		self.mFrameWidth = 0
		self.mFrameRect = None

	def Duck(self):
		self.mImage = self.mDuckImage
		self.mCollisionRect.height = 88
		self.SetPosition([ self.mPosition[0], self.mGroundLevel - self.mRect.height ])
		self.mFrameRect = pygame.Rect(0, 0, 128, 128)
		self.mFrameWidth = 128

	def Run(self):
		self.mImage = self.mRunImage
		self.mRect.height = 128
		self.mFrameWidth = 128
		self.mFrameRect = pygame.Rect(0, 0, 128, 128)

	def Update(self, delta):
		self.mVelocity[1] += self.mGravity 
		self.mPosition[1] += self.mVelocity[1] 

		if self.mPosition[1] > self.mGroundLevel - self.mRect.height:
			self.mPosition[1] = self.mGroundLevel - self.mRect.height

			if (self.mJumpCount > 0):
				self.mJumpCount = 0
				self.Run()

			self.mVelocity[1] = 0

		#Scrolling
		self.mPosition[0] += self.mLevel.mScrollSpeed


		self.mGravity = 1



		self.mCollisionRect.topleft = self.mPosition
		self.mCollisionRect.top += 8
		self.mCollisionRect.left += 10
		Entity.Update(self, delta)  


	

