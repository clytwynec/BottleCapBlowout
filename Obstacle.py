from Entity import *

class Obstacle(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)

	def CheckCollision(self, other):
		if not other.IsA('Obstacle') and not other.IsA('Collectable'):
			return Entity.CheckCollision(self, other)

	def OnCollision(self, other):
		return
