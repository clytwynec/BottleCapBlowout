from GS_MenuBase import *
from Level import *

class GS_MainMenu(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "MainMenu", kernel, gsm)

		kernel.ImageManager().LoadImage("resume.bmp")

	def Initialize(self):
		self.mLevel = Level(self.mKernel, 800)
		self.mLevel.LoadLevel("MainMenu.lvl")


		startHeight = 300
		offset = 75
		count = 0

		self.mHeading, self.mHeadingRect = self.mKernel.ImageManager().LoadImage("heading.bmp")
		self.mHeadingRect.topleft = (400 - self.mHeadingRect.width / 2, 50)

		self.mMenuImages["NewGame"], self.mMenuRects["NewGame"] = self.mKernel.ImageManager().LoadImage("newgame.bmp")
		self.mMenuRects["NewGame"].topleft = (400 - self.mMenuRects["NewGame"].width / 2, startHeight + offset * count)
		self.mMenuItems["NewGame"] = self.mMenuImages["NewGame"]
		count += 1

		self.mMenuImages["Tutorial"], self.mMenuRects["Tutorial"] = self.mKernel.ImageManager().LoadImage("tutorial.bmp")
		self.mMenuRects["Tutorial"].topleft = (400 - self.mMenuRects["Tutorial"].width / 2, startHeight + offset * count)
		self.mMenuItems["Tutorial"] = self.mMenuImages["Tutorial"]
		count += 1

		self.mMenuImages["EditorMenu"], self.mMenuRects["EditorMenu"] = self.mKernel.ImageManager().LoadImage("editor.bmp")
		self.mMenuRects["EditorMenu"].topleft = (780 - self.mMenuRects["EditorMenu"].width, 550)
		self.mMenuItems["EditorMenu"] = self.mMenuImages["EditorMenu"]

		self.mMenuImages["HighScores"], self.mMenuRects["HighScores"] = self.mKernel.ImageManager().LoadImage("highscore_small.bmp")
		self.mMenuRects["HighScores"].topleft = (20, 550)
		self.mMenuItems["HighScores"] = self.mMenuImages["HighScores"]

		self.mMenuImages["Exit"], self.mMenuRects["Exit"] = self.mKernel.ImageManager().LoadImage("exit.bmp")
		self.mMenuRects["Exit"].topleft = (400 - self.mMenuRects["Exit"].width / 2, startHeight + offset * count)
		self.mMenuItems["Exit"] = self.mMenuImages["Exit"]
		count += 1

		GS_MenuBase.Initialize(self)

	def Unpause(self):
		if "Game" not in self.mMenuImages and self.mGameStateManager.GetState("Game").IsInitialized():
			self.mMenuImages["Game"], self.mMenuRects["Game"] = self.mKernel.ImageManager().LoadImage("resume.bmp")
			self.mMenuRects["Game"].topleft = (400 - self.mMenuRects["Game"].width / 2, 225)
			self.mMenuItems["Game"] = self.mMenuImages["Game"]

		GS_MenuBase.Unpause(self)


	def HandleEvent(self, event):
		if (event.type == MOUSEBUTTONDOWN):
			if (self.mMenuRects["NewGame"].collidepoint(event.pos)):
				self.mGameStateManager.GetState("Game").Destroy()
				self.mGameStateManager.SwitchState("Game")
				return

		return GS_MenuBase.HandleEvent(self, event)

	def Update(self, delta):
		#self.mLevel.Scroll(1)
		self.mLevel.Draw()
		self.mLevel.Blit()

		GS_MenuBase.Update(self, delta)