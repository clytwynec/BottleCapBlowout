from GS_MenuBase import *
from Level import *

class HighScores(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "HighScores", kernel, gsm)

	def Initialize(self):
		GS_MenuBase.Initialize(self)

		self.mHighScores = []
		self.LoadScores()

		self.mMenuImages["MainMenu"], self.mMenuRects["MainMenu"] = self.mKernel.ImageManager().LoadImage("mainmenu_small.bmp")
		self.mMenuRects["MainMenu"].topleft = (780 - self.mMenuRects["MainMenu"].width, 500)

		self.mFont = pygame.font.SysFont("Helvetica", 20, True)


	def LoadScores(self):
		HighScoreFile = os.path.join("data", "highscores.txt")
		with open(HighScoreFile) as highscores:
				scoreList = highscores.read().splitlines() 

				for i in range(0, len(scoreList)):
					LevelScores = scoreList[i].split()

					self.mHighScores.append({ 
						"Level" : LevelScores[0], 
						"Score" : str(LevelScores[1])  
					}) 

	def HandleEvent(self, event):

		return GS_MenuBase.HandleEvent(self, event)


	def Unpause(self):
		if "Game" not in self.mMenuImages and self.mGameStateManager.GetState("Game").IsInitialized():
			self.mMenuImages["Game"], self.mMenuRects["Game"] = self.mKernel.ImageManager().LoadImage("resume.bmp")
			self.mMenuRects["Game"].topleft = (400 - self.mMenuRects["Game"].width / 2, 225)
			self.mMenuItems["Game"] = self.mMenuImages["Game"]

		GS_MenuBase.Unpause(self)
		

	def Update(self, delta):
		Top = 40
		Left = 280
		for i in range(0, len(self.mHighScores)):
			textSurface = self.mFont.render(str(self.mHighScores[i]["Level"])[0:-4]+ ":  " + str(self.mHighScores[i]["Score"]), True, Colors.WHITE)
			self.mKernel.DisplaySurface().blit(textSurface, (Left, Top, textSurface.get_rect().width, textSurface.get_rect().height))
			Top += 25

		GS_MenuBase.Update(self, delta)