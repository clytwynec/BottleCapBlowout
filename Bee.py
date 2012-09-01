import math
from Entity import *

class Bee(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Bee1.bmp")
		self.mSolid = 1
		self.mTime = 0

		self.mFloatMax = 5
		self.mFloatDistance = 0
		self.mModifier = 1

	def OnCollision(self, other):
		print "BUZZ BUZZ"

	def Update(self, delta):
		self.mFloatDistance += (self.mModifier)

		if (abs(self.mFloatDistance) >= self.mFloatMax):
			self.mModifier *= -1

		self.mPosition[1] = self.mPosition[1] + self.mFloatDistance

		return Entity.Update(self, delta)