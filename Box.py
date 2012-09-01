from math import sin
from Entity import *

class Box(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel)

		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Box1.bmp")
		self.mSolid = 1
		self.mTime = 0

	def OnCollision(self, other):
		print "Ouch, a box!!"

	def Update(self, delta):

		return Entity.Update(self, delta)