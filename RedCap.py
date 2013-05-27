from BottleCap import *

class RedCap(BottleCap):
	def __init__(self, kernel, level):
		BottleCap.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("BottlecapRed.bmp")
		self.mValue = 5
