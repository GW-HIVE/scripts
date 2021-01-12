import sys
from io import StringIO

from lxml import etree
from optparse import OptionParser

__version__ = "1.0"
__status__ = "Dev"

"""
This script will print(std out) some domains of a .xml file.
This script has three options, you can execute the script in three ways:
1. python xml-parser.1.py --version
This is the option that show you the program's version.
2. python xml-parser.1.py -h
This can show you some help information.
3. python xml-parser.1.py -i <filename.xml>
-i specifies input
This option will open the .xml file you input.
If the element tag is "book", it will output all the attributes of elements. 
If the element tag is "title", it will output the text of the elements.
Usage:
python xml-parser.1.py -i <filename.xml>
"""


def main():
    """sample"""
    usage = "\n%prog  [options]"
    parser = OptionParser(usage, version="%prog " + __version__)
    parser.add_option("-i", "--xmlFile", action="store", dest="xmlFile", help="Input xml file")

    (options, args) = parser.parse_args()
    for file in ([options.xmlFile]):
        if not file:
            parser.print_help()
            sys.exit(0)

    xml_file = options.xmlFile

    fr = open(xml_file)
    xml = fr.read()
    fr.close()

    context = etree.iterparse(StringIO(xml), events=("start", "end"))

    for action, elem in context:
        if action == "start":
            if elem.tag == "book":
                print(elem.attrib["id"])
            elif elem.tag == "title":
                print(elem.text)


if __name__ == '__main__':
    main()
