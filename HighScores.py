from GS_MenuBase import *
from Level import *

class HighScores(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "HighScores", kernel, gsm)

	def Initialize(self):
		GS_MenuBase.Initialize(self)
		self.mHighScores = {}
		self.mMenuImages["MainMenu"], self.mMenuRects["MainMenu"] = self.mKernel.ImageManager().LoadImage("mainmenu.bmp")
		self.mMenuRects["MainMenu"].topleft = (780 - self.mMenuRects["MainMenu"].width, 500)


	def LoadScores(self):
		HighScoreFile = os.path.join("data", highscores.txt)
		with open(HighScoreFile) as highscores:
				scoreList = highscores.read().splitlines() 

				for i in range(0, len(scoreList)):
					LevelScores = scoreList[i].split()

					self.mHighScores.append({ 
						"Level" : parts[0], 
						"Score" : [ int(parts[1]), int(parts[2]) ] 
					}) 

	def HandleEvent(self, event):

		
		return GS_MenuBase.HandleEvent(self, event)

	def Update(self, delta):
		Top = 25
		Left = 250
		for i in range(0, len(self.mHighScores)):
			textSurface = self.mFont.render( + str(self.mBalloon.mValue), True, Colors.WHITE)
			self.mKernel.DisplaySurface().blit(textSurface, (Left, Top, textSurface.get_rect().width, textSurface.get_rect().height))
			Top += 15

		GS_MenuBase.Update(self, delta)