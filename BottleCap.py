
from Collectable import *

class BottleCap(Collectable):
	def __init__(self, kernel, level):
		Collectable.__init__(self, kernel, level)
		self.mCollideSound = self.mKernel.SoundManager().LoadSound("ding.wav")
		self.mSolid = 1
		self.mFloatMax = 0
		self.mFloatDistance = 0
		self.mModifier = 0

	def Update(self, delta):
		self.mFloatDistance += (self.mModifier)

		if (abs(self.mFloatDistance) >= self.mFloatMax):
			self.mModifier *= -1

		self.mPosition[0] = self.mPosition[0] + self.mFloatDistance

		return Collectable.Update(self, delta)

		