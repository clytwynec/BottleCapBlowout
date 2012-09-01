class Entity:
	def __init__(self, kernel, level):
		self.mKernel = kernel
		self.mLevel = level

		self.mSolid = 0
		self.mPosition = [0, 0]

		self.mImage = None
		self.mRect = None
		self.mCollisionRect = None

	def Position(self):
		return self.mPosition

	def SetPosition(self, pos):
		self.mPosition = pos
		self.mRect.topleft = (self.mPosition[0], self.mPosition[1])

	def IsA(self, classname):
		module = __import__(classname)
		_Classname = getattr(module, classname)
		return isinstance(self, _Classname)

	def Rect(self):
		return self.mRect

	def CheckCollision(self, other):
		return self.mRect.colliderect(other.Rect())

	def Update(self, delta):
		self.mRect.topleft = (self.mPosition[0], self.mPosition[1])
		return

	def OnCollision(self, other):
		return

	def Draw(self):
		if (self.mImage):
			self.mLevel.DisplaySurface().blit(self.mImage, self.mRect)
		return
