import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("samplexml.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)   # first child: <person>

    # get a list of XML tags form teh document and print each one
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    # create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","jQuery")
    doc.firstChild.appendChild(newSkill)

    print()
    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()