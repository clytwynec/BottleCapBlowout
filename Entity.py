class Entity:
	def __init__(self, kernel):
		self.mKernel = kernel

		self.mSolid = 0
		self.mPosition = (0, 0)

		self.mImage = None
		self.mRect = None
		self.mCollisionRect = None

	def Update(self, delta):
		return

	def OnCollision(self, other):
		return

	def Draw(self):
		return
