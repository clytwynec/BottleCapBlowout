
from Entity import *

class Balloon(Entity):

	def __init__(self, kernel):
		Entity.__init__(self, kernel)
		self.mValue = 0

	def OnCollision(self, other):
		if other.IsA('Collectable'):
			UpdateBasket(other.mValue)

		if other.IsA('Obstacle'):
			BalloonPop()

		return


	def BalloonPop():
		return


 	def UpdateBasket(CapVal):
 		return

			
