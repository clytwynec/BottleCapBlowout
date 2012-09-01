from Entity import *

class Person(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("Box1.bmp")
		self.mVelocity =  [0,0]
		self.mGravity = 1
		self.mGroundLevel = 500 

	def OnCollision(self, other):
		
		if other.IsA('Collectable'):
			UpdateScore(other.mValue)

		if other.IsA('Obstacle'):
			UpdateScore(other.mValue)

		return



	def UpdateScore(PointsVal):
		score += PointsVal
		return score



	def Update(self, delta):
		
		self.mVelocity[1] += self.mGravity 
		self.mPosition[1] += self.mVelocity[1] 
		if self.mPosition[1] > self.mGroundLevel:
			self.mPosition[1] = self.mGroundLevel
			self.mVelocity[1] = 0
		Entity.Update(self, delta)  

	

