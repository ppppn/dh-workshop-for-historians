from datetime import datetime
from argparse import ArgumentParser
import csv
import glob
import xml.etree.ElementTree as ET
import os
import re


DEFAULT_INPUT_DIRECTORY_PATH = './xml/'
DEFAULT_OUTPUT_CSV_PATH = './output.csv'
argparser = ArgumentParser()
argparser.add_argument(
    '-d',
    '--input-directory',
    type=str,
    dest='input_dir_path',
    default=DEFAULT_INPUT_DIRECTORY_PATH,
    help='specify the directory which the program find xml files.'
)
argparser.add_argument(
    '-o',
    '--output-csv-path',
    type=str,
    dest='csv_path',
    default=DEFAULT_OUTPUT_CSV_PATH,
    help='specify the path of the csv file to output.'
)


xml_path = '../1440-05-16_1_0_13_14_0_7_7.xml'
replace_tags = (
    (re.compile('<hi.*?>(.*?)</hi>', flags=re.MULTILINE),''),
    (re.compile('<ref.*?>(.*?)</ref>', flags=re.MULTILINE), ''),
    (re.compile('<note.*?>(.*)</note>', flags=re.MULTILINE),
                ' (Note: \\1) '),
                )


class CEIdoc:
    def __init__(self,
                 title=None,
                 issuer=None,
                 date_range_start=None,
                 date_range_end=None,
                 location_dict=None,
                 abstract=None):
        """

        :param str title:
        :param str issuer
        :param datetime date_range_start:
        :param datetime date_range_end:
        :param str place_name:
        :param dict location_dict:
        :param str abstract:
        """
        self.title = title
        self.issuer = issuer
        self.date_range_start= date_range_start
        self.date_range_end = date_range_end
        self.location_dict = location_dict
        self.abstract = abstract


def preprocess_xml_text(xml_text):
    """preprocess_xml_text
- replace tags
    - examples:
        - '<note>comment</note>' with '(Note: comment)')
        - remove <ref>, <hi>
    :param str xml_text:
    :rtype: str
    :return: preprocessed xml text
    """
    for comp, repl in replace_tags:
        xml_text = comp.sub(repl, xml_text)

    return xml_text


def parse_xml_to_CEIdoc(root):
    """parse_xml_to_CEIdoc
- read xml root and convert it to a single CEIdoc
    :param root:
    :rtype: CEIdoc
    :return:
    """
    paths = {
        'title': 'teiHeader/fileDesc/titleStmt/title',
        'issuer': 'charter/chDesc/relevantPersonal/issuer/persName',
        'date_range': 'charter/chDesc/head/issued/issueDate/p/dateRange',
        'place_name': 'charter/chDesc/head/issued/issuePlace/placeName',
        'place_loc': 'charter/chDesc/head/issued/issuePlace/location/geo',
        'abstract': 'charter/chDesc/abstract/p',
    }

    title = root.findall(paths['title'])[0].text
    issuer = root.findall(paths['issuer'])[0].text
    date_range_start_str = root.findall(paths['date_range'])[0].attrib['from']
    date_range_end_str = root.findall(paths['date_range'])[0].attrib['to']
    date_range_start = datetime.strptime(date_range_start_str, '%Y-%m-%d')
    date_range_end = datetime.strptime(date_range_end_str, '%Y-%m-%d')
    location_dict = {}
    if root.findall(paths['place_name']):
        location_dict.update({
            'name': root.findall(paths['place_name'])[0].text,
        })
    else:
        location_dict.update({
            'name': 'No Data'
        })
    if root.findall(paths['place_loc']):
        location_dict.update({
            'geo': root.findall(paths['place_loc'])[0].text,
        })
    else:
        location_dict.update({
            'geo': 'No Data'
        })
    abstract_paragraphs = [
        paragraph.text for paragraph in root.findall(paths['abstract'])
    ]
    abstract = ''
    for paragraph in abstract_paragraphs:
        abstract += paragraph + '\n'
    abstract = abstract[:-1]
    cei_doc = CEIdoc(
        title=title,
        issuer=issuer,
        date_range_start=date_range_start,
        date_range_end=date_range_end,
        location_dict=location_dict,
        abstract=abstract
    )
    return cei_doc


def write_to_csv(csv_path, doc_list):
    """write_to_csv
- write CEIdocs' data into a CSV with a header line
    :param: str csv_path:
    :param list[CEIdoc] doc_list:
    :return:
    """
    with open(csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file, lineterminator='\r\n')
        header = ['title', 'issuer', 'date_range_from', 'date_range_to',
                  'place_name', 'place_loc', 'abstract']
        writer.writerow(header)
        for doc in doc_list:
            content = [e for e in (doc.title, doc.issuer, doc.date_range_start,
                                   doc.date_range_end,
                                   doc.location_dict['name'],
                                   doc.location_dict['geo'],
                                   doc.abstract)]
            writer.writerow(content)


def main():
    args = argparser.parse_args()
    input_dir_path = args.input_dir_path
    csv_path = args.csv_path
    if not input_dir_path[-1] == '/':
        input_dir_path += '/'
    if not os.path.isdir(input_dir_path):
        print('invalid input directory path. Abort!')
        return False
    doc_list = []
    file_list = glob.glob(input_dir_path+'*.xml')
    for xml_path in file_list:
        with open(xml_path, 'r', encoding='utf-8') as xml_file:
            xml_text = xml_file.read()
        xml_text = preprocess_xml_text(xml_text)
        root = ET.fromstring(xml_text)
        cei_doc = parse_xml_to_CEIdoc(root)
        doc_list.append(cei_doc)

    write_to_csv(csv_path, doc_list)


if __name__ == '__main__':
    main()