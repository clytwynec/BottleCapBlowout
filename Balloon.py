import math
from Entity import *

class Balloon(Entity):

	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Balloon1.bmp")
		#self.mCollideSound =
		self.mValue = 0
		self.mBlown = 0  # 0 = blower off, 1 = blower on
		self.mGravity = 20 #slope
		self.mBlowStrength = 1
		self.mTicker = 0 #adjust gravity to be less than 1 pixel/frame
		self.mVelocity =  [0, 0]

		self.mMaxBob = 50
		self.mBob = 0
		self.mBobDirecton = 1

	def OnCollision(self, other):
		if other.IsA('Collectable'):
			UpdateBasket(other.mValue)

		if other.IsA('Obstacle'):
			BalloonPop(self)

		return


	def BalloonPop(self):
		#self.mCollideSound.play()
		self.mValue = 0 
		return


 	def UpdateBasket(self, capVal):
 		self.mValue += capVal 
 		self.mGravity += .5
 		return


 	def Update(self, delta):
 		if self.mBlown == 0:
			self.mVelocity[0] = -1 * float(self.mGravity) / delta
			self.mPosition[0] += self.mVelocity[0]

			self.mVelocity[1] = float(self.mGravity) / delta
			self.mPosition[1] += self.mVelocity[1]

			if self.mPosition[1] > self.mGroundLevel:
				self.mPosition[1] = self.mGroundLevel
				self.mPosition[0] -= self.mVelocity[0]

 		elif self.mBlown == 1:
 			 	self.mVelocity[0] += float(self.mBlowStrength) / delta
 			 	self.mVelocity[1] += -1.0 * float(self.mBlowStrength) / delta

				self.mPosition[1] += self.mVelocity[1] 
				self.mPosition[0] += self.mVelocity[0]

				if self.mPosition[1] < 0:
					self.mPosition[1] = 0
					self.mPosition[0] -= self.mVelocity[0]


		oldBob = self.mBob
		self.mBob = self.mMaxBob * math.sin(math.radians(self.mTicker % 360))
		self.mDelta = self.mBob - oldBob

		self.mPosition[0] += self.mDelta

 		self.mTicker += 1

 		# Scrolling
 		self.mPosition[0] += 1

		Entity.Update(self, delta)  

			
