from BottleCap import *

class GoldCap(BottleCap):
	def __init__(self, kernel, level):
		BottleCap.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("BottlecapGold.bmp")
		self.mValue = 15
