from math import cos
from Entity import *

class BottleCap(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Bottlecap.bmp")
		self.mSolid = 1
		self.mTime = 0

	def OnCollision(self, other):
		print "Ouch, a box!!"

	def Update(self, delta):
		self.mTime += delta

		self.mPosition[0] = int(float(self.mPosition[0]) + cos(self.mTime))

		return Entity.Update(self, delta)