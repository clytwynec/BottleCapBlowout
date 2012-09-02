import pygame
from Obstacle import *

class Hive(Obstacle):
	def __init__(self, kernel, level):
		Obstacle.__init__(self, kernel, level)
		self.mImage, self.mImageRect = self.mKernel.ImageManager().LoadImage("hive.bmp")
		self.mRect = pygame.Rect(0, 0, 128, 320)
		#self.mCollideSound =
		self.mSolid = 1
		self.mTime = 0
		self.mValue = -15

		self.mFrameRect = pygame.Rect(0, 0, 128, 320)
		self.mAnimationSpeed = 10
		self.mFrameWidth = 128

	#def OnCollision(self, other):
		#print "Ouch, a box!!"
		## Audio and Animations here

	def Update(self, delta):

		return Obstacle.Update(self, delta)