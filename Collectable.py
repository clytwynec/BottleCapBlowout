from Entity import *

class Collectable(Entity):
	def __init__(self, kernel):
		Entity.__init__(self, kernel

			
	def OnCollision(self, other):
		if !other.IsA('Obstacle'):
			Level.RemoveEntity(self)
		return
