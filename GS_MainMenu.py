from GS_MenuBase import *
from Level import *

class GS_MainMenu(GS_MenuBase):
	def __init__(self, kernel, gsm):
		GS_MenuBase.__init__(self, "MainMenu", kernel, gsm)

	def Initialize(self):
		self.mLevel = Level(self.mKernel, 800)
		self.mLevel.LoadLevel("MainMenu.lvl")

		self.mHeading, self.mHeadingRect = self.mKernel.ImageManager().LoadImage("heading.bmp")
		self.mHeadingRect.topleft = (400 - self.mHeadingRect.width / 2, 50)

		self.mMenuImages["Game"], self.mMenuRects["Game"] = self.mKernel.ImageManager().LoadImage("newgame.bmp")
		self.mMenuRects["Game"].topleft = (400 - self.mMenuRects["Game"].width / 2, 200)

		self.mMenuImages["Tutorial"], self.mMenuRects["Tutorial"] = self.mKernel.ImageManager().LoadImage("tutorial.bmp")
		self.mMenuRects["Tutorial"].topleft = (400 - self.mMenuRects["Tutorial"].width / 2, 300)

		self.mMenuImages["EditorMenu"], self.mMenuRects["EditorMenu"] = self.mKernel.ImageManager().LoadImage("editor.bmp")
		self.mMenuRects["EditorMenu"].topleft = (780 - self.mMenuRects["EditorMenu"].width, 550)

		self.mMenuImages["Exit"], self.mMenuRects["Exit"] = self.mKernel.ImageManager().LoadImage("exit.bmp")
		self.mMenuRects["Exit"].topleft = (400 - self.mMenuRects["Exit"].width / 2, 400)

	def Update(self, delta):
		#self.mLevel.Scroll(1)
		self.mLevel.Draw()
		self.mLevel.Blit()

		GS_MenuBase.Update(self, delta)