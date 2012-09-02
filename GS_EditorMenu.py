from GS_MenuBase import *
from Level import *
from GS_Editor import *

import Colors

import os

class GS_EditorMenu(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "EditorMenu", kernel, gsm)

	def Initialize(self):
		self.mLevel = Level(self.mKernel, 800)
		self.mLevel.LoadLevel("MainMenu.lvl")

		self.mFont = pygame.font.SysFont('Arial', 24, True)

		path = os.path.join("data", "levels")
		filecount = 0
		for filename in os.listdir(path):
			if ("lvl" in filename):
				self.mMenuImages["Edit_" + filename] = self.mFont.render("Edit " + filename, True, Colors.WHITE)
				self.mMenuRects["Edit_" + filename] = self.mMenuImages["Edit_" + filename].get_rect()
				self.mMenuRects["Edit_" + filename].topleft = (100, 100 + 35 * filecount)
				filecount += 1

		self.mMenuImages["Edit_Level" + str(filecount) + ".lvl"] = self.mFont.render("New Level: Level" + str(filecount) + ".lvl", True, Colors.WHITE)
		self.mMenuRects["Edit_Level" + str(filecount) + ".lvl"] = self.mMenuImages["Edit_Level" + str(filecount) + ".lvl"].get_rect()
		self.mMenuRects["Edit_Level" + str(filecount) + ".lvl"].topleft = (100, 55)

		self.mMenuImages["MainMenu"], self.mMenuRects["MainMenu"] = self.mKernel.ImageManager().LoadImage("mainmenu.bmp")
		self.mMenuRects["MainMenu"].topleft = (780 - self.mMenuRects["MainMenu"].width, 500)

	def HandleEvent(self, event):
		if event.type == MOUSEBUTTONDOWN:
			for item in self.mMenuRects:
				if ("Edit_" in item and self.mMenuRects[item].collidepoint(event.pos)):
						levelName = item.split("_")[1]

						if (self.mGameStateManager.GetState("Editor")):
							self.mGameStateManager.DeregisterState("Editor")

						self.mGameStateManager.RegisterState(GS_Editor(self.mKernel, self.mGameStateManager, levelName))
						self.mGameStateManager.SwitchState("Editor")
						return

		GS_MenuBase.HandleEvent(self, event)

	def Update(self, delta):

		GS_MenuBase.Update(self, delta)