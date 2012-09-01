import os
import pygame

from pygame.locals import *

class Level:
	def __init__(self, kernel, screenSize):
		self.mKernel = kernel

		self.mLevelEntities = []
		self.mEntities = []

		self.mBackgroundImageName = ''

		self.mLevelLength = 0
		self.mLevelName = ""
		self.mLevelSurface = None

		self.mScrenSize = screenSize

		self.mLevelHeight = 768

		self.mBackgroundImage, self.mBackgroundRect = kernel.ImageManager().LoadImage("bg_test.bmp", False)

		self.mCameraX = 0

		return

	def DisplaySurface(self):
		return self.mLevelSurface

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
	def LoadLevel(self, levelName, levelLength = 0):
		self.mLevelName = levelName
		self.mLevelLength = int(levelLength)

		fullLevelName = os.path.join("data", "levels", levelName)

		if os.path.isfile(fullLevelName):

			with open(fullLevelName) as levelList:
				entityList = levelList.read().splitlines() 

				self.mBackgroundImageName = entityList[0]
				self.mLevelLength = int(entityList[1])

				if (self.mLevelLength == 0):
					self.mLevelLength = 2046

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
		# Set the level surface correctly:
		print self.mLevelLength, self.mLevelHeight
		self.mLevelSurface = pygame.Surface((self.mLevelLength, self.mLevelHeight))

		# Spin through the loaded entities, eval them, and split them into collidable and other entities
		if (len(self.mLevelEntities) > 0):
			for entity in self.mLevelEntities:
				# get the module name, and dynamically instantiate the class
				mod = __import__(entity["name"])
				EntityClass_ = getattr(mod, entity["name"])

				rawEntity = EntityClass_(self.mKernel, self)

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
			file.write(self.mBackgroundImageName + "\n")
			file.write(str(self.mLevelLength) + "\n")

			for entity in self.mEntities:
				file.write(entity.__class__.__name__ + " ")
				file.write(str(entity.Position()[0]) + " ")
				file.write(str(entity.Position()[1]) + "\n")

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

	def ScreenToLevelCoordinates(self, screenCoord):
		return [ screenCoord[0] + self.mCameraX, screenCoord[1] ]

	def Scroll(self, amount):
		self.mCameraX += amount
		if (self.mCameraX < 0):
			self.mCameraX = 0
		elif (self.mCameraX > (self.mLevelLength - self.mScrenSize):
			self.mCameraX = self.mLevelLength

	##############################################
	# Draw
	#
	# Draw the entities of the level and the level
	# itself
	##############################################
	def Draw(self):
		self.mLevelSurface.blit(self.mBackgroundImage, self.mBackgroundRect)

		for entity in self.mEntities:
			entity.Draw()

		self.mKernel.DisplaySurface().blit(self.mLevelSurface, self.mKernel.DisplaySurface().get_rect(), pygame.Rect(self.mCameraX, 0, 1024, self.mLevelHeight))

		return
