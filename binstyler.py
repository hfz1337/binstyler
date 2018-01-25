from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from random import randrange as rand
from math import sqrt, ceil
import sys
import os

def banner():
	print("======================================================")
	print("| Image to binary style converter made by 0xdeadbeef |")
	print("| Contact: gh_zouahi@esi.dz                          |")
	print("======================================================")

def usage():
	print("Usage: python binstyler.py input_image -o output_image -s font_size")
	print("       input_image and output_image can be a full path.")
	print("       font_size > 0")
	print("       Example: python binstyler.py image.jpg -o new_image.jpg -s 10")

def error():
	print("An error has occured, please make sure:")
	print("  [X] - To specify the full image name ( with the extension included )")
	print("  [X] - That the image's path is valid and that the image exists")
	print("  [X] - That the font size is greater than 0")
	usage()


def brightness(red,green,blue):
	return sqrt(0.241*(red**2) + 0.691*(green**2) + 0.068*(blue**2) )

def main():
	if len(sys.argv)!=6 or sys.argv[2]!="-o" or sys.argv[4]!="-s" or int(sys.argv[5])<1:
		banner()
		usage()
	else:
		try:
			img = Image.open(sys.argv[1])
			
			pixel_array = list(img.getdata())
			width, height = img.size
			pixel_array = [pixel_array[i * width:(i + 1) * width] for i in range(height)]

			font_size = int(sys.argv[5])

			w = ceil(font_size*0.875)
			h = ceil(font_size*0.825)

			img = Image.new("RGB", [width,height], (0,0,0))

			draw = ImageDraw.Draw(img)
			font = ImageFont.truetype("consola.ttf", font_size)

			binary = ["0","1"]

			i,j = 0,0

			while i < height:
				while j < width:

					red = pixel_array[i][j][0]
					green = pixel_array[i][j][1]
					blue = pixel_array[i][j][2]

					if brightness(red,green,blue) > 127:
						draw.text((j, i),binary[rand(2)],(255,255,255),font=font)

					j += w

				i += h
				j = 0

			img.save(sys.argv[3])

			print("New image saved as " + sys.argv[3])
		except:
			error()
			
if __name__ ==	"__main__":
	main()