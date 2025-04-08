import xml.etree.ElementTree as ET

tree=ET.parse('data.xml')
print(type(tree))
root=tree.getroot()
print(type(root))
print(root.tag)
print(str(root.attrib))
