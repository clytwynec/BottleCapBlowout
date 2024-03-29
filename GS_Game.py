import pygame
import os
import math
from Person import *
from Balloon import *
from GameState import *
from Level import *
from pygame.locals import *
import Colors

class GS_Game(GameState):
	def __init__(self, kernel, gsm):
		GameState.__init__(self, "Game", kernel, gsm)

		self.mLevelName = ""
		self.mLevel = None

		self.mGroundLevel = 570

		self.mHighScores = {}

		self.mScrollSpeed = 2

		self.mPaused = 0

		self.mHouse = None

		self.mCurrentLevel = 1
		self.mLevelComplete = False
		self.mSoundState = 1

		self.mMusic = self.mKernel.SoundManager().LoadSound("BGmusic_flyaway.wav")

		self.mGameOverImage, self.mGameOverRect = self.mKernel.ImageManager().LoadImage("gameover.bmp")
		self.mLevelCompleteImage, self.mLevelCompleteRect = self.mKernel.ImageManager().LoadImage("levelcomplete.bmp")
		self.mMainMenuImage, self.mMainMenuRect = self.mKernel.ImageManager().LoadImage("mainmenu_small.bmp")
		self.mNextLevelImage, self.mNextLevelRect = self.mKernel.ImageManager().LoadImage("nextlevel.bmp")
		self.mHighScoreImage, self.mHighScoreRect = self.mKernel.ImageManager().LoadImage("highscore_alert.bmp")

		self.mGameOverRect.topleft = (400 - self.mGameOverRect.width / 2, 150)
		self.mLevelCompleteRect.topleft = (400 - self.mLevelCompleteRect.width / 2, 50)
		self.mHighScoreRect.topleft = (400 - self.mHighScoreRect.width / 2, 225)
		self.mNextLevelRect.topleft = (600 - self.mMainMenuRect.width / 2, 350)
		self.mMainMenuRect.topleft = (400 - self.mMainMenuRect.width / 2, 350)

		self.mFont = pygame.font.SysFont("Helvetica", 16, True)

		self.mPreviousPop = False
		self.mPreviousDead = 0
		self.mCurrentLevel = 1

		self.mNextLevelName = ""

	def Initialize(self, levelName = ""):
		self.mHighScores = {}
		self.mScore = 0
		self.mPaused = 0

		if (levelName):
			self.LoadLevel(levelName)

			if (levelName[5].isdigit()):
				self.mCurrentLevel = int(levelName[5])
			else:
				self.mCurrentLevel = -1

		elif (self.mNextLevelName):
			self.LoadLevel(self.mNextLevelName)
		else:
			self.LoadLevel("Level1")

		self.LoadScores()

		self.mLevelComplete = False

		for entity in self.mLevel.mEntities:
			entity.mSoundState = self.mSoundState

		self.mBalloon.mSoundState = self.mSoundState
		self.mPerson.mSoundState = self.mSoundState

		self.mMusic.set_volume(.3 * self.mSoundState)
		self.mMusic.stop()
		self.mMusic.play(-1)


		fullLevelName = os.path.join("data", "levels", "Level" + str(self.mCurrentLevel + 1) + ".lvl")
		if os.path.isfile(fullLevelName):
			self.mNextLevelName = "Level" + str(self.mCurrentLevel + 1)
			self.mMainMenuRect.topleft = (200 - self.mMainMenuRect.width / 2, 350)
		else:
			self.mNextLevelName = ""
			self.mMainMenuRect.topleft = (400 - self.mMainMenuRect.width / 2, 350)

		return GameState.Initialize(self)

	def LoadLevel(self, levelName):
		self.mLevelName = levelName + ".lvl"
		self.mLevel = Level(self.mKernel, 800)

		self.mLevel.LoadLevel(self.mLevelName)
		self.mLevel.mScrollSpeed = self.mScrollSpeed

		self.mCordImage, self.mCordRect = self.mKernel.ImageManager().LoadImage("cord.bmp")
		self.mCordRect.bottomleft = (0, self.mGroundLevel)

		self.mPerson = Person(self.mKernel, self.mLevel)
		self.mPerson.SetPosition([128, self.mGroundLevel])
		self.mPerson.mScreenOffset = 128
		self.mPerson.SetGroundLevel(self.mGroundLevel)
		self.mPerson.SyncCollisionRect()

		self.mHouse = House(self.mKernel, self.mLevel)
		self.mHouse.SetPosition([ self.mLevel.mLevelLength - 512, self.mGroundLevel - 480 ])
		self.mHouse.SyncCollisionRect()

		self.SpawnBalloon()

	def SpawnBalloon(self):
		self.mBalloon = Balloon(self.mKernel, self.mLevel)
		self.mBalloon.SetPosition([ self.mLevel.mCameraX + self.mPerson.mScreenOffset + 128, self.mGroundLevel - self.mBalloon.Rect().height - 128 ])
		self.mBalloon.mGroundLevel = 500

	def Destroy(self):
		self.mMusic.stop()
		self.mNextLevelName = ""
		self.mCurrentLevel = 1
		return GameState.Destroy(self)

	def Pause(self):
		self.mMusic.stop()
		return GameState.Pause(self)

	def Unpause(self):
		self.mMusic.play(-1)
		return GameState.Unpause(self)


	def HandleEvent(self, event):
		if (event.type == QUIT):
			pygame.quit()
			sys.exit()
		elif (event.type == KEYDOWN):
			if (event.key == K_UP):
				self.mPerson.Jump()
			elif (event.key == K_DOWN):
				self.mPerson.Duck()
			elif (event.key == K_SPACE):
				self.mBalloon.mBlown = 1
			elif (event.key == K_p):
				self.mPaused = (self.mPaused + 1) % 2
			elif (event.key == K_ESCAPE):	
				self.mGameStateManager.SwitchState('MainMenu')
			elif (event.key == K_m):
				for entity in self.mLevel.mEntities:
					entity.mSoundState = (entity.mSoundState +1) % 2
				self.mBalloon.mSoundState = (self.mBalloon.mSoundState +1) % 2
				self.mPerson.mSoundState = (self.mBalloon.mSoundState + 1) % 2
				self.mSoundState = (self.mSoundState +1) % 2
				self.mMusic.set_volume(.3*self.mSoundState)


		elif(event.type == KEYUP):
			if (event.key == K_SPACE):
				self.mBalloon.mBlown = 0  
			elif (event.key == K_DOWN):
				self.mPerson.Run()

		elif (event.type == MOUSEBUTTONDOWN):
			if (self.mMainMenuRect.collidepoint(event.pos)):
				self.Destroy()
				self.mGameStateManager.SwitchState("MainMenu")
			elif (self.mNextLevelRect.collidepoint(event.pos)):
				self.mCurrentLevel += 1
				self.Initialize()

		return GameState.HandleEvent(self, event)

	def Update(self, delta):
		if (not self.mLevelComplete):
			if self.mPerson.CheckCollision(self.mHouse):
				self.mLevelComplete = True
				self.SaveScore()
				self.mPerson.Done()

		if self.mLevel.mCameraX > (self.mLevel.mLevelLength - 1500):
			self.mBalloon.mBlown = 0

		if not self.mLevelComplete and self.mPaused == 0:
			if (self.mPerson.mDead == 0 and self.mPerson.mLives > 0):
				self.mLevel.Scroll(self.mScrollSpeed)

			self.mLevel.Update(delta)

			if (self.mPerson.mLives > 0):
				self.mPerson.Update(delta)

			if (self.mPerson.mDead == 0):# and self.mPerson.mLives > 0):
				self.mBalloon.Update(delta)

			if (self.mPerson.CheckCollision(self.mBalloon) and self.mBalloon.CheckCollision(self.mPerson)):
				self.mPerson.OnCollision(self.mBalloon)
				self.mBalloon.OnCollision(self.mPerson)

			self.mLevel.CheckCollisions(self.mPerson)
			self.mLevel.CheckCollisions(self.mBalloon)
					

			if (self.mBalloon.mPopped):
				if (not self.mPreviousPop):
					self.mPerson.mLives -= 1

				if (self.mBalloon.mPosition[0] < self.mLevel.mCameraX):
					if (self.mPerson.mLives > 0):
						self.SpawnBalloon()

			if (self.mPerson.mResetting):
				self.SpawnBalloon()
				self.mPerson.mResetting = False
			
		self.mLevel.Draw()

		self.mHouse.DrawBack()

		self.mCordRect.bottomright = self.mPerson.Rect().bottomleft
		self.mLevel.DisplaySurface().blit(self.mCordImage, self.mCordRect)
		self.mPerson.Draw()
		self.mHouse.Draw()
		self.mBalloon.Draw()

		self.mLevel.Blit()

		textSurface = self.mFont.render( str(self.mLevelName)[0:-4], True, Colors.WHITE)
		self.mKernel.DisplaySurface().blit(textSurface, (30, 580, textSurface.get_rect().width, textSurface.get_rect().height))
		
		textSurface = self.mFont.render("Score: " + str(self.mPerson.mScore), True, Colors.WHITE)
		self.mKernel.DisplaySurface().blit(textSurface, (150, 580, textSurface.get_rect().width, textSurface.get_rect().height))
		
		textSurface = self.mFont.render("Lives: " + str(self.mPerson.mLives), True, Colors.WHITE)
		self.mKernel.DisplaySurface().blit(textSurface, (270, 580, textSurface.get_rect().width, textSurface.get_rect().height))

		textSurface = self.mFont.render("In Basket: " + str(self.mBalloon.mValue), True, Colors.WHITE)
		self.mKernel.DisplaySurface().blit(textSurface, (390, 580, textSurface.get_rect().width, textSurface.get_rect().height))

		textSurface = self.mFont.render("Points Possible: " + str(self.mLevel.mMaxScore), True, Colors.WHITE)
		self.mKernel.DisplaySurface().blit(textSurface, (540, 580, textSurface.get_rect().width, textSurface.get_rect().height))
		
		if (self.mPerson.mLives == 0):
			self.mKernel.DisplaySurface().blit(self.mGameOverImage, self.mGameOverRect)
			
			self.mMainMenuRect.topleft = (400 - self.mMainMenuRect.width / 2, 350)
			self.mKernel.DisplaySurface().blit(self.mMainMenuImage, self.mMainMenuRect)

		if (self.mLevelComplete):
			self.mKernel.DisplaySurface().blit(self.mLevelCompleteImage, self.mLevelCompleteRect)
			self.mKernel.DisplaySurface().blit(self.mMainMenuImage, self.mMainMenuRect)

			if (self.mHighScores[self.mLevelName]  == self.mPerson.mScore):
				self.mKernel.DisplaySurface().blit(self.mHighScoreImage, self.mHighScoreRect)

			if (self.mNextLevelName != ""):
				self.mKernel.DisplaySurface().blit(self.mNextLevelImage, self.mNextLevelRect)

		self.mPreviousDead = self.mPerson.mDead
		self.mPreviousPop = self.mBalloon.mPopped
		
		return GameState.Update(self, delta)

	def SaveScore(self):
		if self.mLevelName in self.mHighScores:
			if self.mPerson.mScore > self.mHighScores[self.mLevelName]:
				self.mHighScores[self.mLevelName] = self.mPerson.mScore
		else:
			self.mHighScores[self.mLevelName] = self.mPerson.mScore

		with open(os.path.join("data", "highscores.txt"), 'w') as file:
			for level in self.mHighScores:
				file.write(level + " " + str(self.mHighScores[level]) + "\n")

	def LoadScores(self):
		HighScoreFile = os.path.join("data", "highscores.txt")
		if (os.path.isfile(HighScoreFile)):
			with open(HighScoreFile) as highscores:
					scoreList = highscores.read().splitlines() 

					for i in range(0, len(scoreList)):
						parts = scoreList[i].split()

						self.mHighScores[parts[0]] = int(parts[1])