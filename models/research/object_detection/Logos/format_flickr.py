import os
import xml.etree.cElementTree as ET
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()

imagesDir = 'flickr_logos_27_dataset_images'
annotFile = 'flickr_logos_27_dataset_training_set_annotation.txt'
for filename in os.listdir('images\\' + imagesDir):
	imageName = filename
	imageFolder = 'images\\' + imagesDir

	#get heigth and width of image
	im = Image.open('images\\' + imagesDir + '\\' + imageName, "r")
	imageWidth, imageHeight = im.size
	depth = "3"

	#make XML
	annotation = ET.Element("annotation", verified="yes")

	ET.SubElement(annotation, "folder").text = imageFolder
	ET.SubElement(annotation, "filename").text = imageName
	ET.SubElement(annotation, "path").text = dir_path + '\\' + 'images\\' + imagesDir + '\\' + imageName

	source = ET.SubElement(annotation, "source")
	ET.SubElement(source, "database").text = 'Unknown'

	size = ET.SubElement(annotation, "size")
	ET.SubElement(size, "width").text = str(imageWidth)
	ET.SubElement(size, "height").text = str(imageHeight)
	ET.SubElement(size, "depth").text = depth

	ET.SubElement(annotation, "segmented").text = '0'

	# this all because files show up multiple times
	tempB1List = []
	with open('images\\' + annotFile,'r') as f:
		for line in f:
			boxList = line.split()
			# print(boxList)
			if boxList[0] == imageName and boxList[3] not in tempB1List:
				tempB1List.append(boxList[3])
				print('we can create object')

				theObject = ET.SubElement(annotation, "object")
				ET.SubElement(theObject, "name").text = boxList[1].lower()
				ET.SubElement(theObject, "pose").text = 'Unspecified'
				ET.SubElement(theObject, "truncated").text = '0'
				ET.SubElement(theObject, "difficult").text = '0'

				bndbox = ET.SubElement(theObject, "bndbox")
				ET.SubElement(bndbox, "xmin").text = boxList[3]
				ET.SubElement(bndbox, "ymin").text = boxList[4]
				ET.SubElement(bndbox, "xmax").text = boxList[5]
				ET.SubElement(bndbox, "ymax").text = boxList[6]

	#save xml
	tree = ET.ElementTree(annotation)
	tree.write("annotations\\flickr\\" + imageName + '.xml')
