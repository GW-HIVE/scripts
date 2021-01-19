"""
This script will print(std out) some domains of a .xml file.

Input:
######

    * -i : specified input file

Output:
#######

    * Some domains of a .xml file

Usage:
#######

    * python xml-parser.py --version

    * This is the option that show you the program's version.*

    * python xml-parser.py -h

    * This can show you some help information.*

    * python xml-parser.1.py -i <filename.xml>

   *Runs program with specified input file*

"""
import sys
from io import StringIO
from argparse import ArgumentParser
from lxml import etree  # pylint: disable=import-error


__version__ = "1.0"
__status__ = "Dev"


def main():
    """Finds and prints XML domains"""
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)
    parser.add_argument("-i", "--xmlFile", action="store", dest="xmlFile", help="Input xml file")

    options = parser.parse_args()
    for file in [options.xmlFile]:
        if not file:
            parser.print_help()
            sys.exit(0)

    xml_file = options.xmlFile

    file_reader = open(xml_file)
    xml = file_reader.read()
    file_reader.close()

    context = etree.iterparse(StringIO(xml), events=("start", "end"))

    for action, elem in context:
        if action == "start":
            if elem.tag == "book":
                print(elem.attrib["id"])
            elif elem.tag == "title":
                print(elem.text)


if __name__ == '__main__':
    main()
