
from Entity import *

class Balloon(Entity):

	def __init__(self, kernel):
		Entity.__init__(self, kernel)
		#self.mCollideSound =
		self.mValue = 0

	def OnCollision(self, other):
		if other.IsA('Collectable'):
			UpdateBasket(other.mValue)

		if other.IsA('Obstacle'):
			BalloonPop(self)

		return


	def BalloonPop(self):
		#self.mCollideSound.play()
		self.mValue = 0 
		return


 	def UpdateBasket(CapVal):
 		self.mValue += CapVal 
 		return

			
