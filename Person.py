from Entity import *

class Person(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel)


	def OnCollision(self, other):
		if other.IsA('Collectable'):
			UpdateScore(other.mValue)

		if other.IsA('Obstacle'):

		return

	def UpdateScore(PointsVal):
		score += PointsVal