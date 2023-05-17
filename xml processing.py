import xml.sax
import xml.dom.minidom

# using sax
class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("-------------PERSON------------")
            print("ID:{}".format(attrs['id']))

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))
        elif self.current == "name":
            print("Age: {}".format(self.age))
        elif self.current == "name":
            print("Weight: {}".format(self.weight))
        elif self.current == "name":
            print("Height: {}".format(self.height))
        self.current = ""

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')


# using dom
domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print("-----------PERSON------------")
    if person.hasAttribute('id'):
        print("")
        print("ID: {}".format(person.getAttribute(('id'))))

    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Name"
persons[0].setAttribute('id', '100 ')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "18"
domtree.writexml(open('data.xml','w'))

newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Green'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('23'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('180'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('174'))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)
domtree.writexml(open('data.xml','w'))
