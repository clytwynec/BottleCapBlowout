class Level:
	def __init__(self, kernel):
		self.mRawLevelEntities = []
		self.mLevelEntities = []
		self.mCollidableEntities = []
		self.mBackgroundImageName = ''
		return

	def LoadLevel(self, levelName):
		levelList = open('levelName')
		entityList = levelList.read.splitlines() 
		for i in range(1, len(entityList)):
			parts = entityList[i].split()
			self.mLevelEntities.append({name:parts[0], position:(part[1], part[2])}) 
		return

	def ProcessEntities(self):

		return
		
	def Update(self, delta):

		return

	def Draw(self):

		return
