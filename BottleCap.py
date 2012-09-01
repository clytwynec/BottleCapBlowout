from math import cos
from Entity import *

class BottleCap(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Bottlecap.bmp")
		self.mSolid = 1
		self.mFloatMax = 3
		self.mFloatDistance = 0
		self.mModifier = 1

	def OnCollision(self, other):
		print "Ding!"

	def Update(self, delta):
		self.mFloatDistance += (self.mModifier)

<<<<<<< local
		#self.mPosition[0] = int(float(self.mPosition[0]) + cos(self.mTime))
=======
		if (abs(self.mFloatDistance) >= self.mFloatMax):
			self.mModifier *= -1
>>>>>>> other

		self.mPosition[0] = self.mPosition[1] + self.mFloatDistance

		return Entity.Update(self, delta)

		