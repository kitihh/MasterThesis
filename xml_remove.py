#!/usr/bin/env python3

from xml.etree import ElementTree as ET

fname = "annotations11"
label = "Carright3"

root = ET.parse((fname + '.xml')).getroot()
print(root)

for image in root.findall("image"): # direct children of root
    for polygon in image.findall("polygon"): # direct children of images
        x = polygon.attrib.get("label")
        if x != label:
            image.remove(polygon)
            #print("Removed")

et = ET.ElementTree(root)
et.write(fname + '_' + label + '.xml')