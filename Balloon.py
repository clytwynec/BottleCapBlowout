import math
from Entity import *

class Balloon(Entity):

	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Box1.bmp")
		#self.mCollideSound =
		self.mValue = 0
		self.mBlown = 0  # 0 = blower off, 1 = blower on
		self.mGravity = 0 #slope
		self.mBlowStrength = 3
		self.mTicker = 0 #adjust gravity to be less than 1 pixel/frame
		self.mVelocity =  [0, 0]

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
 			if self.mTicker % 10 == 0:
 				self.mVelocity[0] = -1*math.floor(self.mGravity)
 				self.mVelocity[1] = math.floor(self.mGravity)
				self.mPosition[1] += self.mVelocity[1] 
				self.mPosition[0] += self.mVelocity[0]

				if self.mPosition[1] > self.mGroundLevel:
					self.mPosition[1] = self.mGroundLevel
					self.mPosition[0] -= self.mVelocity[0]

 		elif self.mBlown == 1:
 			 	self.mVelocity[0] = self.mBlowStrength
 			 	self.mVelocity[1] = -1*self.mBlowStrength
				self.mPosition[1] += self.mVelocity[1] 
				self.mPosition[0] += self.mVelocity[0]

				if self.mPosition[1] < 0:
					self.mPosition[1] = 0
					self.mPosition[0] -= self.mVelocity[0]  

 		self.mTicker += 1

		Entity.Update(self, delta)  

			
