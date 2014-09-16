import os, sys
from PIL import Image, ImageFile
from exceptions import IOError

try:
	img = Image.open(sys.argv[1])
	outSize = int(input("size:"))
	imgInit = 0
	outImgL = imgInit
	outImgT = imgInit
	outImgR = imgInit + outSize
	outImgD = imgInit + outSize
	imgCutRtime = img.size[0] // outSize
	imgCutDtime = img.size[1] // outSize
	imgCut = imgCutRtime * imgCutDtime
	j = 1
	k = 1
	#path = "_"
	ImageFile.MAXBLOCK = img.size[0] * img.size[1]

	for inFile in sys.argv[1:]:
		for i in range(1, imgCut):
			if k > imgCutDtime :
				outImgL += outSize
				outImgT = imgInit
				outImgR += outSize
				outImgD = outSize
				j += 1
				k = 1
			box = (outImgL, outImgT ,outImgR, outImgD)
			region = img.crop(box)
			#im2.paste(region, box)
			outImgT += outSize
			outImgD += outSize
			outFile = os.path.splitext(inFile)[0] + "_" + str(j) + "_" + str(k) + ".png"
			if inFile != outFile:
				region.save(outFile, "PNG", quality=90, optimize=True, progressive=False)
				k += 1

	print("Succeed")

except IOError:
	print("Failed")
	pass