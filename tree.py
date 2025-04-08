import xml.etree.ElementTree as ET
xml='''\
<?xml version="1.0"?>
<data 名稱="e-happy">
    <person 姓名="David">
        <身高>183</身高>
    </person>
</data>

'''

root=ET.fromstring(xml)
print(type(root))
print(root.tag)
print(str(root.attrib))
print(str(root.text))
print(str(root.get('名稱')))
root.set('名稱','文淵閣工作室')
print(str(root.get('名稱')))