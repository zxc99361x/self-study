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
person=root.find('person')
print("find:"+person[0].text)

person=root.findall('person')
print("findall:"+person[1][1].text)

persons=list(root.iter(tag='person'))
for person in persons:
    print(f"tag:{person.tag} attrib: {person.attrib}")
    tall=person.find("身高").text
    hobby=person.find("興趣").text
    print(f"身高:{tall} 興趣:{hobby}")