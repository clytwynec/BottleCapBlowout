from Entity import *

class Collectable(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)


	def OnCollision(self, other):
		if not other.IsA('Obstacle'):
			if self.mCollideSound:
				self.mCollideSound.play()
			Level.RemoveEntity(self)
		return
