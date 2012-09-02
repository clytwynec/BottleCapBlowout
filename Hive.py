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

		self.mCollisionRect = pygame.Rect(0, 0, 64, 64)

	#def OnCollision(self, other):
		#print "Ouch, a box!!"
		## Audio and Animations here

	def Update(self, delta):
		self.mCollisionRect.topleft = (self.mRect.left, self.mRect.top + 60)

		return Obstacle.Update(self, delta)