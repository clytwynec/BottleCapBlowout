from Entity import *

class Collectable(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)
		self.mCollideSound = None

	def CheckCollision(self, other):
		if not other.IsA('Obstacle') and not other.IsA('Collectable'):
			return Entity.CheckCollision(self, other)


	def OnCollision(self, other):
		if not other.IsA('Obstacle'):
			if self.mCollideSound:
				if self.mSoundState == 1:
					self.mCollideSound.play()
			self.mLevel.RemoveEntity(self)
		return
