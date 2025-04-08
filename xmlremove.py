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
root[0].set('姓名','鮭魚')
hobby=root[0].find('興趣')
hobby.text="跑馬拉松"

root.remove(root[1])

tree=ET.ElementTree(root)
tree.write("newdata2.xml",encoding="UTF-8")