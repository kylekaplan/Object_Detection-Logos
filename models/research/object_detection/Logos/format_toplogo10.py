import os
import xml.etree.cElementTree as ET
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

masksDir = 'qmul_toplogo10\masks'
for folder in os.listdir('images\\' + masksDir):
	for filename in os.listdir('images\\' + 'qmul_toplogo10\masks\\' + folder):

# for filename in os.listdir('images\qmul_toplogo10\masks\\test'):
		print(filename)

		# read file
		f=open('images\\' + masksDir + '\\' + folder + '\\' + filename, "r")
		contents = f.read()
		boxList = contents.split()

		#remove extension to get imageName
		extPos = filename.find('.bboxes.txt')
		
		imageName = filename[:extPos]
		imageFolder = 'images\qmul_toplogo10\jpg\\' + folder
		#get heigth and width of image
		im = Image.open('images\qmul_toplogo10\jpg\\' + folder + '\\' + imageName, "r")
		imageWidth, imageHeight = im.size
		depth = "3"
		
		#make XML
		annotation = ET.Element("annotation", verified="yes")

		ET.SubElement(annotation, "folder").text = imageFolder
		ET.SubElement(annotation, "filename").text = imageName
		ET.SubElement(annotation, "path").text = dir_path + '\\' + 'images\qmul_toplogo10\jpg\\' + folder + '\\' + imageName

		source = ET.SubElement(annotation, "source")
		ET.SubElement(source, "database").text = 'Unknown'

		size = ET.SubElement(annotation, "size")
		ET.SubElement(size, "width").text = str(imageWidth)
		ET.SubElement(size, "height").text = str(imageHeight)
		ET.SubElement(size, "depth").text = depth

		ET.SubElement(annotation, "segmented").text = '0'

		theObject = ET.SubElement(annotation, "object")
		ET.SubElement(theObject, "name").text = folder
		ET.SubElement(theObject, "pose").text = 'Unspecified'
		ET.SubElement(theObject, "truncated").text = '0'
		ET.SubElement(theObject, "difficult").text = '0'

		bndbox = ET.SubElement(theObject, "bndbox")
		ET.SubElement(bndbox, "xmin").text = boxList[0]
		ET.SubElement(bndbox, "ymin").text = boxList[1]
		ET.SubElement(bndbox, "xmax").text = str(int(boxList[2]) + int(boxList[0]))
		ET.SubElement(bndbox, "ymax").text = str(int(boxList[3]) + int(boxList[1]))

		#save xml
		tree = ET.ElementTree(annotation)
		tree.write("annotations\\" + imageName + '.xml')
