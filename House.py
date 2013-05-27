from Entity import *
import pygame

class House(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mBackImage, backRect = self.mKernel.ImageManager().LoadImage("house_back.bmp")
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("house_front.bmp")

		self.mCollisionRect = pygame.Rect(0, 0, 64, 600)

	def Update(self, delta):
		self.SyncCollisionRect()

		return Entity.Update(self, delta)

	def SyncCollisionRect(self):
		self.mCollisionRect.topleft = (self.mPosition[0] + 380, 0)


	def DrawBack(self):
		self.mLevel.DisplaySurface().blit(self.mBackImage, self.mRect)