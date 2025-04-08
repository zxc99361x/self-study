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

root=ET.fromstring(xml)
person=ET.Element("person")
person.attrib={"姓名":"Tsjeng"}
tall=ET.Element("身高")
tall.text="176"
hobby=ET.Element("興趣")
hobby="圍棋"
root.append(person)
print(root[2].get('姓名'))