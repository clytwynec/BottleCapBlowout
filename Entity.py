class Entity:
	def __init__(self, kernel, level):
		self.mKernel = kernel
		self.mLevel = level

		self.mSolid = 0
		self.mPosition = [0, 0]

		self.mImage = None
		self.mImageRect = None
		self.mFrameRect = None
		self.mRect = None
		self.mCollisionRect = None

		self.mFrameWidth = 0
		self.mAnimationSpeed = 1
		self.mAnimationTick = 0

	def Position(self):
		return self.mPosition

	def SetPosition(self, pos):
		self.mPosition = pos
		self.mRect.topleft = (self.mPosition[0], self.mPosition[1])

	def IsA(self, classname):
		module = __import__(classname)
		_Classname = getattr(module, classname)
		return isinstance(self, _Classname)

	def CollisionRect(self):
		if (self.mCollisionRect): 
			return self.mCollisionRect

		return self.mRect

	def Rect(self):
		return self.mRect

	def CheckCollision(self, other):
		if (self.mCollisionRect):
			return self.mCollisionRect.colliderect(other.CollisionRect())
			
		return self.mRect.colliderect(other.CollisionRect())

	def Update(self, delta):
		self.mAnimationTick += 1

		self.mRect.topleft = (self.mPosition[0], self.mPosition[1])

		if (self.mFrameWidth and self.mAnimationTick > self.mAnimationSpeed):
			self.mAnimationTick = 0
			self.mFrameRect.move_ip((self.mFrameWidth, 0))

			if (self.mFrameRect.right > self.mImage.get_rect().width):
				self.mFrameRect.left = 0

		return

	def OnCollision(self, other):
		return

	def Draw(self):
		if (self.mImage):
			if (self.mFrameRect):
				self.mLevel.DisplaySurface().blit(self.mImage, self.mRect, self.mFrameRect)
			else:
				self.mLevel.DisplaySurface().blit(self.mImage, self.mRect)
		return
