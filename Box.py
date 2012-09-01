from math import sin
from Entity import *

class Box(Obstacle):
	def __init__(self, kernel, level):
		Obstacle.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Box1.bmp")
		#self.mCollideSound =
		self.mSolid = 1
		self.mTime = 0

	#def OnCollision(self, other):
		#print "Ouch, a box!!"
		## Audio and Animations here

	def Update(self, delta):

		return Obstacle.Update(self, delta)