from Entity import *
import pygame

class Person(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mRunImage, self.mRunRect = self.mKernel.ImageManager().LoadImage("player_run.bmp")
		self.mDuckImage, self.mDuckRect = self.mKernel.ImageManager().LoadImage("player_duck.bmp")
		self.mJumpImage1, self.mJumpRect1 = self.mKernel.ImageManager().LoadImage("player_jump1.bmp")
		self.mJumpImage2, self.mJumpRect2 = self.mKernel.ImageManager().LoadImage("player_jump2.bmp")
		self.mDeadImage, deadRect = self.mKernel.ImageManager().LoadImage("player_dead.bmp")
		self.mBlowImage, deadRect = self.mKernel.ImageManager().LoadImage("player_blow.bmp")
		self.mFinishedImage, deadRect = self.mKernel.ImageManager().LoadImage("player_done.bmp")


		self.mDuckHeight = 88
		self.mStandHeight = 115

		self.mImage = self.mRunImage
		self.mRect = pygame.Rect(0, 0, 128, 128)
		self.mCollisionRect = pygame.Rect(0, 0, 60, self.mStandHeight)

		self.mScreenOffset = 0

		self.mVelocity =  [0,1]

		self.mGravity = 1

		self.mGroundLevel = 0
		self.mScore = 0
		self.mJumpCount = 0
		self.mPause = 0

		self.mLives = 5

		self.mFrameRect = pygame.Rect(0, 0, 128, 128)
		self.mFrameWidth = 128
		self.mAnimationSpeed = 4

		self.mResetting = False
		self.mStopped = False
		self.mDead = 0

	def OnCollision(self, other):
		if other.IsA('Collectable'):
			self.UpdateScore(other.mValue)
		elif other.IsA('Obstacle'):
			self.UpdateScore(other.mValue)


		if other.IsA('Obstacle'):
			self.UpdateScore(other.mValue)

			if (other.mDeadly):
				self.mDead = 2000
				self.Reset()
			elif (other.mSolid):
				if (self.mVelocity[1] >= 0 and self.mCollisionRect.bottom - other.CollisionRect().top <= 16):
					if (self.mJumpCount > 0):
						self.mJumpCount = 0
						self.Run()

					self.mVelocity[1] = 0
					self.mGravity = 0
					self.mPosition[1] -= self.mCollisionRect.bottom - other.CollisionRect().top - 1
				elif (self.mCollisionRect.right - other.CollisionRect().left > 0):
					self.mStopped = True


		if other.IsA('Balloon'):
			self.UpdateScore(other.mValue)

		return

	def SetGroundLevel(self, groundLevel):
		self.mGroundLevel = groundLevel

	def UpdateScore(self, pointsVal):
		self.mScore += pointsVal
		return self.mScore

	def Jump(self):
		if self.mDead == 0 and self.mJumpCount < 2:
			self.mJumpCount +=1
			self.mVelocity[1] = -15

			if (self.mJumpCount == 1):
				self.mImage = self.mJumpImage1
			else:
				self.mImage = self.mJumpImage2

			self.mCollisionRect.height = self.mStandHeight
			self.mFrameWidth = 0
			self.mFrameRect = None

	def Duck(self):
		if (self.mJumpCount == 0 and self.mDead == 0):
			self.mImage = self.mDuckImage

			self.mCollisionRect.height = self.mDuckHeight

			self.mFrameRect = pygame.Rect(0, 0, 128, 128)
			self.mAnimationSpeed = 4
			self.mFrameWidth = 128

	def Run(self):
		if (self.mJumpCount == 0 and self.mDead == 0):
			self.mImage = self.mRunImage
			self.mCollisionRect.height = self.mStandHeight
			self.mFrameWidth = 128
			self.mFrameRect = pygame.Rect(0, 0, 128, 128)
			self.mAnimationSpeed = 4

	def Done(self):
		self.mImage = self.mFinishedImage
		self.mFrameWidth = 0
		self.mFrameRect = None #pygame.Rect(0, 0, 128, 128)
		self.mFrameWidth = 0

	def SyncCollisionRect(self):
		self.mCollisionRect.left = self.mPosition[0] + 10
		self.mCollisionRect.bottom = self.mPosition[1] + self.mRect.height - 10
		self.mCollisionRect.left += 10

	def Reset(self):
		if (self.mLives > 0):
			self.SetPosition([ max(0, self.mPosition[0] - 100), self.mPosition[1] ])
			self.mLevel.mCameraX = max(0, self.mPosition[0] - self.mScreenOffset)
			self.mImage = self.mDeadImage
			self.mFrameWidth = 128
			self.mFrameRect = pygame.Rect(0, 0, 128, 128)
			self.mVelocity[1] = 0
			self.mResetting = True
			self.mJumpCount = 0
			self.mLives -= 1

			self.Run()

	def Update(self, delta):
		wasDead = self.mDead > 0
		self.mDead = max(0, self.mDead - delta)

		if (not self.mStopped and self.mPosition[0] < self.mScreenOffset + self.mLevel.mCameraX):
			distDelta = min(self.mScreenOffset + self.mLevel.mCameraX - self.mPosition[0], 2)
			self.mVelocity[0] = distDelta * self.mLevel.mScrollSpeed
		elif (self.mStopped):
			self.mVelocity[0] = -1 * self.mLevel.mScrollSpeed

		if (self.mPosition[0] + self.mRect.width - self.mLevel.mCameraX < 0):
		 	if (self.mLives > 1):
				self.mDead = 2000
				self.Reset()
			elif (self.mLives > 0):
				self.mDead = 10000
				self.mLives -= 1

		if (self.mDead <= 0):
			self.mVelocity[1] += self.mGravity 
			self.mPosition[1] += self.mVelocity[1] 

			if self.mPosition[1] > self.mGroundLevel - self.mRect.height:
				self.mPosition[1] = self.mGroundLevel - self.mRect.height

				if (self.mJumpCount > 0):
					self.mJumpCount = 0
					self.Run()

				self.mVelocity[1] = 0

			#Scrolling
			self.mPosition[0] += self.mVelocity[0] + self.mLevel.mScrollSpeed

		elif (wasDead and self.mDead <= 0):
			self.Run()

		# Reset Stuffs
		self.mVelocity[0] = 0
		self.mGravity = 1
		self.mStopped = False

		self.SyncCollisionRect()
		
		Entity.Update(self, delta)  


	

