from GS_MenuBase import *
from Level import *
from GS_Editor import *

import Colors

import os

class GS_LevelSelect(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "LevelSelect", kernel, gsm)

	def Initialize(self):
		self.mFont = pygame.font.SysFont('Helvetica', 24, True)

		loading = self.mFont.render("Loading...", True, Colors.WHITE)
		self.mKernel.DisplaySurface().blit(loading, (400 - loading.get_rect().width / 2, 300 - loading.get_rect().height / 2, loading.get_rect().width, loading.get_rect().height))
		self.mKernel.FlipDisplay()

		self.mHeading, self.mHeadingRect = self.mKernel.ImageManager().LoadImage("levelselect.bmp")
		self.mHeadingRect.topleft = (400 - self.mHeadingRect.width / 2, 50)

		path = os.path.join("data", "levels")
		filecount = 0
		for filename in os.listdir(path):
			if ("lvl" in filename):
				filename = filename[0:-4]
				self.mMenuImages["Game_" + filename] = self.mFont.render(filename, True, Colors.WHITE)
				self.mMenuRects["Game_" + filename] = self.mMenuImages["Game_" + filename].get_rect()
				self.mMenuRects["Game_" + filename].topleft = (200, 150 + 35 * filecount)
				filecount += 1

		self.mMenuImages["MainMenu"], self.mMenuRects["MainMenu"] = self.mKernel.ImageManager().LoadImage("mainmenu.bmp")
		self.mMenuRects["MainMenu"].topleft = (780 - self.mMenuRects["MainMenu"].width, 500)

		GS_MenuBase.Initialize(self)

	def HandleEvent(self, event):
		if event.type == MOUSEBUTTONDOWN:
			for item in self.mMenuRects:
				if ("Game_" in item and self.mMenuRects[item].collidepoint(event.pos)):
						levelName = item.split("_")[1]
						
						self.mGameStateManager.GetState("Game").Destroy()
						self.mGameStateManager.GetState("Game").Initialize(levelName)
						self.mGameStateManager.SwitchState("Game")
						return

		GS_MenuBase.HandleEvent(self, event)

	def Update(self, delta):

		GS_MenuBase.Update(self, delta)