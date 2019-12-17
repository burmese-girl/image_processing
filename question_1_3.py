import csv
import os
import lxml.etree as etree

mypath = os.path.dirname(os.path.abspath(__file__))

csv.register_dialect('custom', delimiter=',', escapechar=None, quotechar='"', quoting=csv.QUOTE_MINIMAL,
                     skipinitialspace=False)


def convert_CSVtoXML_B_004():

    with open(mypath + '/Question1/Dataset/12163257_B_004_00001.csv', 'r') as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        rows = list(reader)
    inputcsv.close()

    xmlData = open(mypath + '/Question1/Dataset/12163257_B_004_00001_mayyi.xml', 'w')
    xmlData.write('<annotation>' + "\n")

    for row in rows:
        xmlData.write('<object>' + "\n")
        xmlData.write('<tag>' + row[4] + '</tag>\n')
        xmlData.write('<bndbox>' + "\n")
        xmlData.write('<x>' + row[0] + '</x>\n')
        xmlData.write('<y>' + row[1] + '</y>\n')
        xmlData.write('<width>' + row[2] + '</width>\n')
        xmlData.write('<height>' + row[3] + '</height>\n')
        xmlData.write('</bndbox>' + "\n")
        xmlData.write('</object>' + "\n")

    xmlData.write('</annotation>' + "\n")
    print ('Success B_004!')

def convert_CSVtoXML_B_007():

    with open(mypath + '/Question1/Dataset/12163257_B_007_00001.csv', 'r') as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        rows = list(reader)
    inputcsv.close()

    xmlData = open(mypath + '/Question1/Dataset/12163257_B_007_00001_mayyi.xml', 'w')
    xmlData.write('<annotation>' + "\n")

    for row in rows:
        xmlData.write('<object>' + "\n")
        xmlData.write('<tag>' + row[4] + '</tag>\n')
        xmlData.write('<bndbox>' + "\n")
        xmlData.write('<x>' + row[0] + '</x>\n')
        xmlData.write('<y>' + row[1] + '</y>\n')
        xmlData.write('<width>' + row[2] + '</width>\n')
        xmlData.write('<height>' + row[3] + '</height>\n')
        xmlData.write('</bndbox>' + "\n")
        xmlData.write('</object>' + "\n")

    xmlData.write('</annotation>' + "\n")
    print ('Success B_007 !')

def convert_CSVtoXML_B_013():

    with open(mypath + '/Question1/Dataset/12163257_B_013_00001.csv', 'r') as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        rows = list(reader)
    inputcsv.close()

    xmlData = open(mypath + '/Question1/Dataset/12163257_B_013_00001_mayyi.xml', 'w')
    xmlData.write('<annotation>' + "\n")

    for row in rows:
        xmlData.write('<object>' + "\n")
        xmlData.write('<tag>' + row[4] + '</tag>\n')
        xmlData.write('<bndbox>' + "\n")
        xmlData.write('<x>' + row[0] + '</x>\n')
        xmlData.write('<y>' + row[1] + '</y>\n')
        xmlData.write('<width>' + row[2] + '</width>\n')
        xmlData.write('<height>' + row[3] + '</height>\n')
        xmlData.write('</bndbox>' + "\n")
        xmlData.write('</object>' + "\n")

    xmlData.write('</annotation>' + "\n")
    print ('Success B_013 !')

def convert_CSVtoXML_B_017():

    with open(mypath + '/Question1/Dataset/12163257_B_017_00001.csv', 'r') as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        rows = list(reader)
    inputcsv.close()

    xmlData = open(mypath + '/Question1/Dataset/12163257_B_017_00001_mayyi.xml', 'w')
    xmlData.write('<annotation>' + "\n")

    for row in rows:
        xmlData.write('<object>' + "\n")
        xmlData.write('<tag>' + row[4] + '</tag>\n')
        xmlData.write('<bndbox>' + "\n")
        xmlData.write('<x>' + row[0] + '</x>\n')
        xmlData.write('<y>' + row[1] + '</y>\n')
        xmlData.write('<width>' + row[2] + '</width>\n')
        xmlData.write('<height>' + row[3] + '</height>\n')
        xmlData.write('</bndbox>' + "\n")
        xmlData.write('</object>' + "\n")

    xmlData.write('</annotation>' + "\n")
    print ('Success B_017 !')

def convert_CSVtoXML_B_018():

    with open(mypath + '/Question1/Dataset/12163257_B_018_00001.csv', 'r') as inputcsv:
        reader = csv.reader(inputcsv, delimiter=',')
        rows = list(reader)
    inputcsv.close()

    xmlData = open(mypath + '/Question1/Dataset/12163257_B_018_00001_mayyi.xml', 'w')
    xmlData.write('<annotation>' + "\n")

    for row in rows:
        xmlData.write('<object>' + "\n")
        xmlData.write('<tag>' + row[4] + '</tag>\n')
        xmlData.write('<bndbox>' + "\n")
        xmlData.write('<x>' + row[0] + '</x>\n')
        xmlData.write('<y>' + row[1] + '</y>\n')
        xmlData.write('<width>' + row[2] + '</width>\n')
        xmlData.write('<height>' + row[3] + '</height>\n')
        xmlData.write('</bndbox>' + "\n")
        xmlData.write('</object>' + "\n")

    xmlData.write('</annotation>' + "\n")
    print ('Success B_018 !')

# call_methods
convert_CSVtoXML_B_004()
convert_CSVtoXML_B_007()
convert_CSVtoXML_B_013()
convert_CSVtoXML_B_017()
convert_CSVtoXML_B_018()
