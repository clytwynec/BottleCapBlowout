from GS_MenuBase import *
from Level import *

class GS_MainMenu(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "MainMenu", kernel, gsm)

		self.mLevel = Level(kernel, 800)
		self.mLevel.LoadLevel("MainMenu.lvl")

		self.mHeading, self.mHeadingRect = kernel.ImageManager().LoadImage("heading.bmp")
		self.mHeadingRect.topleft = (400 - self.mHeadingRect.width / 2, 50)

		self.mMenuImages["Game"], self.mMenuRects["Game"] = kernel.ImageManager().LoadImage("newgame.bmp")
		self.mMenuRects["Game"].topleft = (400 - self.mMenuRects["Game"].width / 2, 200)

		self.mMenuImages["Tutorial"], self.mMenuRects["Tutorial"] = kernel.ImageManager().LoadImage("tutorial.bmp")
		self.mMenuRects["Tutorial"].topleft = (400 - self.mMenuRects["Tutorial"].width / 2, 300)

		self.mMenuImages["Exit"], self.mMenuRects["Exit"] = kernel.ImageManager().LoadImage("exit.bmp")
		self.mMenuRects["Exit"].topleft = (400 - self.mMenuRects["Exit"].width / 2, 400)

	def Update(self, delta):
		#self.mLevel.Scroll(1)
		self.mLevel.Draw()
		self.mLevel.Blit()

		GS_MenuBase.Update(self, delta)