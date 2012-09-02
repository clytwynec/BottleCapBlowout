import math
import pygame
from Entity import *

class Balloon(Entity):

	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mUnpoppedImage, self.mRect = self.mKernel.ImageManager().LoadImage("balloon.bmp")
		self.mPoppedImage, poppedRect = self.mKernel.ImageManager().LoadImage("balloon_popped.bmp")

		self.mImage = self.mUnpoppedImage

		#self.mCollideSound =
		self.mValue = 0
		self.mBlown = 0  # 0 = blower off, 1 = blower on
		self.mGravity = 15 #slope
		self.mBlowStrength = 3
		self.mTicker = 0 #adjust gravity to be less than 1 pixel/frame
		self.mVelocity =  [0, 0]

		self.mBalloonRect = pygame.Rect(0, 0, 32, 45)
		self.mBucketRect = pygame.Rect(0, 0, 32, 45)

		self.mBalloonRect.topleft = self.mRect.topleft
		self.mBucketRect.bottomleft = self.mRect.bottomleft

		self.mFrameWidth = 32
		self.mFrameRect = pygame.Rect(0, 0, 32, 128)
		self.mAnimationSpeed = 20

		self.mPopped = False

		self.mBlowStartSound = self.mKernel.SoundManager().LoadSound("hairdryer_on.wav")
		self.mBlowEndSound = self.mKernel.SoundManager().LoadSound("hairdryer_off.wav")
		self.mBlowSound = self.mKernel.SoundManager().LoadSound("hairdryer.wav")

		self.mBlowStartSound.set_volume(0.05)
		self.mBlowEndSound.set_volume(0.05)
		self.mBlowSound.set_volume(0.05)

		self.mBlowChannel = None


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
 		self.mBlowStrength -= .25
 		return

 	def EmptyBasket(self):
 		self.mGravity -= 0.5 * self.mValue
 		self.mValue = 0
 		self.mBlowStrength = 20


 	def Update(self, delta):
 		if not self.mPopped:
	 		if self.mBlown == 0:

	 			if (self.mBlowChannel and self.mBlowChannel.get_sound()):
	 				self.mBlowChannel.stop()
	 				self.mBlowChannel = None
	 				self.mBlowEndSound.play()

				self.mVelocity[0] = -1 * float(self.mGravity) / delta
				self.mPosition[0] += self.mVelocity[0]

				self.mVelocity[1] = float(self.mGravity) / delta
				self.mPosition[1] += self.mVelocity[1]

				if self.mPosition[1] > self.mGroundLevel - 120:
				 	self.mPosition[1] = self.mGroundLevel - 120
					self.mPosition[0] -= self.mVelocity[0]
					self.mVelocity = [0, 0]

	 		elif self.mBlown == 1:
	 			if (not self.mBlowChannel):
	 				self.mBlowChannel = self.mBlowStartSound.play()
	 				self.mBlowChannel.queue(self.mBlowSound)
	 			elif (not self.mBlowChannel.get_queue()):
	 				self.mBlowChannel.queue(self.mBlowSound)

				self.mVelocity[0] += float(self.mBlowStrength) / delta
				self.mVelocity[1] += -1.0 * float(self.mBlowStrength) / delta

				self.mPosition[1] += self.mVelocity[1] 
				self.mPosition[0] += self.mVelocity[0]
			
				if self.mPosition[1] > self.mGroundLevel - 120:
					self.mPosition[1] = self.mGroundLevel - 120
					self.mPosition[0] -= self.mVelocity[0]
					self.mVelocity = [0, 0]

				if self.mPosition[1] < 0:
					self.mPosition[1] = 0
					self.mPosition[0] -= self.mVelocity[0]
		else:
			self.mVelocity =[-5,1]
			self.mVelocity[1] += float(self.mGravity) / delta
			self.mPosition[1] += self.mVelocity[1]
			self.mPosition[0] -= self.mVelocity[1]

			if self.mPosition[1] > self.mGroundLevel - 43:
					self.mPosition[1] = self.mGroundLevel - 43
					self.mPosition[0] += self.mVelocity[0]


		self.Scrolling(delta)

 		self.mTicker += 1

		self.mBalloonRect.topleft = self.mRect.topleft
		self.mBucketRect.bottomleft = self.mRect.bottomleft

		Entity.Update(self, delta)  

	def Scrolling(self, delta):
		self.mPosition[0] += self.mLevel.mScrollSpeed
			
