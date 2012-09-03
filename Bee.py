import math
import random
from Obstacle import *

class Bee(Obstacle):
	def __init__(self, kernel, level):
		Obstacle.__init__(self, kernel, level)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Bee1.bmp")
		self.mSolid = 0
		self.mFloatMax = 15
		self.mFloatDistance = random.randrange(-1 * self.mFloatMax, self.mFloatMax)
		self.mModifier = 1
		self.mSharp = 1
		self.mValue = 0
		self.mDeadly = 1

	def OnCollision(self, other):
		##Audio and Animations here 
		return

	def Update(self, delta):
		self.mFloatDistance += (self.mModifier)

		if (abs(self.mFloatDistance) >= self.mFloatMax):
			self.mModifier *= -1

		self.mPosition[1] = self.mPosition[1] + self.mModifier

		return Obstacle.Update(self, delta)
