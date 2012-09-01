import os


class Level:
	def __init__(self, kernel):
		self.mKernel = kernel
		self.mLevelEntities = []
		self.mEntities = []
		self.mBackgroundImageName = ''
		self.mLevelLength = 0
		self.mLevelName = ""

		self.mBackgroundImage, self.mBackgroundRect = kernel.ImageManager().LoadImage("bg_test.bmp", False)
		return

	#############################################
	# LoadLevel
	#
	# Loads a level from a file and puts a
	# raw list of the entity definitions into
	# self.mLevelEntities
	#
	# Parameters:
	#	levelname - the level name (with extension)
	# 		Lives in "data/levels/"
	##############################################
	def LoadLevel(self, levelName):
		self.mLevelName = levelName

		fullLevelName = os.path.join("data", "levels", levelName)

		if os.path.isfile(fullLevelName):

			with open(fullLevelName) as levelList:
				entityList = levelList.read().splitlines() 

				self.mBackgroundImageName = entityList[0]
				self.mLevelLength = entityList[1]

				for i in range(2, len(entityList)):
					parts = entityList[i].split()

					self.mLevelEntities.append({ 
						"name" : parts[0], 
						"position" : [ int(parts[1]), int(parts[2]) ] 
					}) 

		self.ProcessEntities()
		return

	##############################################
	# ProcessEntities
	#
	# Works through the list of raw entities and
	# dynamically instantiates the entity elements
	#
	# Each entity must have a class defined with
	# an Update, OnCollision, and __init__ methods
	##############################################
	def ProcessEntities(self):
		# Spin through the loaded entities, eval them, and split them into collidable and other entities
		if (len(self.mLevelEntities) > 0):
			for entity in self.mLevelEntities:
				# get the module name, and dynamically instantiate the class
				mod = __import__(entity["name"])
				EntityClass_ = getattr(mod, entity["name"])

				rawEntity = EntityClass_(self.mKernel)

				rawEntity.SetPosition(entity["position"])

				self.mEntities.append(rawEntity)

		return

	##############################################
	# SaveLevel
	#
	# Serializes a level to a file
	##############################################
	def SaveLevel(self, levelname):
		lines = []

		with open(os.path.join("data", "levels", levelname), 'w') as file:
			file.write(self.mBackgroundImageName)
			file.write(self.mLevelLength)

			for entity in self.mEntities:
				file.write(entity.__class__.__name__)
				file.write(entity.Position()[0])
				file.write(entity.Position()[1])

	##############################################
	# AddEntity
	#
	# Adds an entity to the level at the given
	# position
	##############################################
	def AddEntity(self, entity, position):
		entity.SetPosition(position)
		self.mEntities.append(entity)

	##############################################
	# RemoveEntity
	#
	# Removes an entity from the level
	##############################################
	def RemoveEntity(entity):
		if (entity in self.mEntities):
			self.mEntities.remove(entity)

	##############################################
	# EntityAt
	# 
	# Given a position, return entity if its
	# rect overlaps that position 
	##############################################
	def EntityAt(self, position):
		for entity in self.mEntities:
			if entity.Rect().collide_point(position):
				return entity
		return


	##############################################
	# CheckCollisions
	#
	# Spins through the entities and checks for
	# collisions with other entities
	##############################################
	def CheckCollisions(self):
		hitPairs = []


	##############################################
	# Update
	#
	# Update the level
	##############################################
	def Update(self, delta):
		for entity in self.mEntities:
			entity.Update(delta)

		return

	##############################################
	# Draw
	#
	# Draw the entities of the level and the level
	# itself
	##############################################
	def Draw(self):
		self.mKernel.DisplaySurface().blit(self.mBackgroundImage, self.mBackgroundRect)

		for entity in self.mEntities:
			entity.Draw()

		return
