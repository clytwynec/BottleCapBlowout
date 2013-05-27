from BottleCap import *

class BlueCap(BottleCap):
	def __init__(self, kernel, level):
		BottleCap.__init__(self, kernel, level)
		self.mImage, self.mRect = self.mKernel.ImageManager().LoadImage("BottlecapBlue.bmp")
		self.mValue = 10


		