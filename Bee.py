from math import sin
from Entity import *

class Bee(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Bee.bmp")
		self.mSolid = 1
		self.mTime = 0

	def OnCollision(self, other):
		print "BUZZ BUZZ"

	def Update(self, delta):
		self.mTime += delta

		self.mPosition[1] += sin(self.mTime)

		return Entity.Update(self, delta)