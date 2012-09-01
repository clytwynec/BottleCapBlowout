from math import cos
from Collectable import *

class BottleCap(Collectable):
	def __init__(self, kernel, level):
		Collectable.__init__(self, kernel, level)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Bottlecap.bmp")
		#self.mCollideSound =
		self.mSolid = 1
		self.mFloatMax = 3
		self.mFloatDistance = 0
		self.mModifier = 1
		self.mValue = 5


	#def OnCollision(self, other):
		#print "Ding!"
		## Audio and Animations here

	def Update(self, delta):
		self.mFloatDistance += (self.mModifier)

		if (abs(self.mFloatDistance) >= self.mFloatMax):
			self.mModifier *= -1

		self.mPosition[0] = self.mPosition[0] + self.mFloatDistance

		return Collectable.Update(self, delta)

		