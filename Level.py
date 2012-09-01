class Level:
	def __init__(self, kernel):
		self.mKernel = []
		self.mLevelEntities = []
		self.mEntities = []
		self.mBackgroundImageName = ''
		self.mLevelLength = 0
		return

	def LoadLevel(self, levelName):
		levelList = open('levelName')
		entityList = levelList.read.splitlines() 
		self.mBackgroundImageName = entityList[0]
		self.mLevelLength = entityList[1]
		for i in range(2, len(entityList)):
			parts = entityList[i].split()
			self.mLevelEntities.append({name:parts[0], position:(part[1], part[2])}) 

		self.ProcessEntities()
		return

	def ProcessEntities(self):
		# Spin through the loaded entities, eval them, and split them into collidable and other entities
		if (len(self.mLevelEntities) > 0):
			for entity in self.mLevelEntities:
				# get the module name, and dynamically instantiate the class
				EntityClass_ = getattr(module, entity)
				rawEntity = EntityClass_(self.mKernel)
				self.mEntities.append(rawEntity)

		return

	def SaveLevel(self, levelname):
		lines = []

		with open("levels/data/" + levelname, 'w') as file:
			file.write(self.mBackgroundImageName)
			file.write(self.mLevelLength)

			for entity in self.mEntities:
				file.write(entity.__class__.__name__)
				file.write(entity.Position()[0])
				file.write(entity.Position()[1])

	def EntityAt(self, position):
		for entity in self.mEntities:
			if entity.Rect().collide_point(position):
				return entity
		return


	def Update(self, delta):
		for entity in self.mEntities:
			entity.Update(delta)

		return

	def Draw(self):
		for entity in self.mEntities:
			entity.Draw()

		return
