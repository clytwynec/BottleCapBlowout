from Entity import *

class Person(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel)
		self.mVelocity =  (0,0)
		self.mGravity = -5
		self.mGroundLevel = 1000 

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
		self.mVelocity += self.mGravity * delta
		self.mPosition += self.mVelocity * delta   

	

