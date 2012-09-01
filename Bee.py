import math
from Entity import *

class Bee(Obstacle):
	def __init__(self, kernel):
		Obstacle.__init__(self, kernel)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Bee1.bmp")
		self.mSolid = 1
		self.mFloatMax = 3
		self.mFloatDistance = 0
		self.mModifier = 1

	def OnCollision(self, other):
		#print "BUZZ BUZZ"
		self.mAudio 

	def Update(self, delta):
		self.mFloatDistance += (self.mModifier)

		if (abs(self.mFloatDistance) >= self.mFloatMax):
			self.mModifier *= -1

		self.mPosition[1] = self.mPosition[1] + self.mFloatDistance

		return Obstacle.Update(self, delta)








