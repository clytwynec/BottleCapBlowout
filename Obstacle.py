from Entity import *

class Obstacle(Entity):
	def __init__(self, kernel, level):
		Entity.__init__(self, kernel, level)


	def OnCollision(self, other):
		return
