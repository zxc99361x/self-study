import xml.etree.ElementTree as ET
xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
        <興趣>長跑</興趣>
    </person>
    <person 姓名="Chiou">
        <身高>170</身高>
        <興趣>籃球</興趣>
    </person>
</data>

'''

#def pretty_xml(element,indent,newline,level=0):


root=ET.fromstring(xml)
person=ET.Element("person")
person.attrib={"姓名":"Tsjeng"}
tall=ET.SubElement(person,"身高")
tall.text="176"
hobby=ET.SubElement(person,"興趣")
hobby="圍棋"
root.insert(0,person)
print(root[0].get('姓名'))

tree=ET.ElementTree(root)
tree.write("newdata.xml",encoding="UTF-8")