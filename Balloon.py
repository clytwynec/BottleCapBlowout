import math
import pygame
from Entity import *

class Balloon(Entity):

	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mUnpoppedImage, self.mRect = self.mKernel.ImageManager().LoadImage("Balloon1.bmp")
		self.mPoppedImage, poppedRect = self.mKernel.ImageManager().LoadImage("balloon_popped.bmp")

		self.mImage = self.mUnpoppedImage

		#self.mCollideSound =
		self.mValue = 0
		self.mBlown = 0  # 0 = blower off, 1 = blower on
		self.mGravity = 20 #slope
		self.mBlowStrength = 1
		self.mTicker = 0 #adjust gravity to be less than 1 pixel/frame
		self.mVelocity =  [0, 0]

		self.mBalloonRect = pygame.Rect(0, 0, 32, 45)
		self.mBucketRect = pygame.Rect(0, 0, 32, 45)

		self.mBalloonRect.topleft = self.mRect.topleft
		self.mBucketRect.bottomleft = self.mRect.bottomleft

		self.mPopped = False


	def CheckCollision(self, other):
		if (not self.mPopped):
			if (other.IsA('Person')):
				return self.mBucketRect.colliderect(other.CollisionRect())
			else:
				return self.mBalloonRect.colliderect(other.CollisionRect())

	def OnCollision(self, other):
		if other.IsA('Collectable'):
			self.UpdateBasket(other.mValue)

		if other.IsA('Obstacle'):
			self.BalloonPop()

		if other.IsA('Person'):
			self.mValue = 0

		return


	def BalloonPop(self):
		#self.mCollideSound.play()
		self.mImage = self.mPoppedImage
		self.mValue = 0 
		self.mPopped = True
		return


 	def UpdateBasket(self, capVal):
 		self.mValue += capVal 
 		self.mGravity += 5
 		return

 	def EmptyBasket(self):
 		self.mGravity -= 0.5 * self.mValue
 		self.mValue = 0


 	def Update(self, delta):
 		if not self.mPopped:
	 		if self.mBlown == 0:
				self.mVelocity[0] = -1 * float(self.mGravity) / delta
				self.mPosition[0] += self.mVelocity[0]

				self.mVelocity[1] = float(self.mGravity) / delta
				self.mPosition[1] += self.mVelocity[1]

				if self.mPosition[1] > self.mGroundLevel - 120:
				 	self.mPosition[1] = self.mGroundLevel - 120
					self.mPosition[0] -= self.mVelocity[0]

	 		elif self.mBlown == 1:
				self.mVelocity[0] += float(self.mBlowStrength) / delta
				self.mVelocity[1] += -1.0 * float(self.mBlowStrength) / delta

				self.mPosition[1] += self.mVelocity[1] 
				self.mPosition[0] += self.mVelocity[0]
			
				if self.mPosition[1] > self.mGroundLevel - 120:
					self.mPosition[1] = self.mGroundLevel - 120
					self.mPosition[0] -= self.mVelocity[0]

				if self.mPosition[1] < 0:
					self.mPosition[1] = 0
					self.mPosition[0] -= self.mVelocity[0]
		else:
			self.mVelocity =[-5,1]
			self.mVelocity[1] += float(self.mGravity) / delta
			self.mPosition[1] += self.mVelocity[1]
			self.mPosition[0] -= self.mVelocity[1]

			if self.mPosition[1] > self.mGroundLevel -43:
					self.mPosition[1] = self.mGroundLevel -43
					self.mPosition[0] += self.mVelocity[0]


		self.Scrolling(delta)

 		self.mTicker += 1

		self.mBalloonRect.topleft = self.mRect.topleft
		self.mBucketRect.bottomleft = self.mRect.bottomleft

		Entity.Update(self, delta)  

	def Scrolling(self, delta):
		self.mPosition[0] += self.mLevel.mScrollSpeed
			
