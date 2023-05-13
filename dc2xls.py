import argparse
from pathlib import Path
from bs4 import BeautifulSoup

# script description
parser = argparse.ArgumentParser(
    prog='dc2xls',
    description='Format Dependency-Check reports into XLS table',
    usage='python3 dc2xls.py --input <input_file> --ouput <output_file>'
)

# arguments
parser.add_argument('--input')
parser.add_argument('--output', default='output.txt')

args = parser.parse_args()

# check if input file exists
if not Path(args.input).is_file():
    raise SyntaxError(f"Can't find {args.input} :(")

soup = BeautifulSoup(open(args.input), 'html_parser')

all_vulnerabilities = []

dependencies_with_vulns = soup.find_all('h3', {'class': 'subsectionheader standardsubsection'})

counter = 1

for dependency in dependencies_with_vulns:
    vulnerability = []
    dependency_details = dependency.findNext('div')
    published_vulns_header = dependency_details.find('h4', string="Published Vulnerabilities")
    dependency_vulns = published_vulns_header.findNext('div')
    p_elements = dependency_vulns.find_all('p')
    for p in p_elements:
        if not "Vulnerable Software" in p.text:
            for ul in p.find_all('ul'):
                ul.decompose()
            vulnerability.append(dependency.text)
            # data is grouped by 3 <p> elements
            data = p.text
            if counter == 1:
                #1 extract CVE number
                pass
            elif counter == 2:
                #2 extract Severity, Score, CWE
                pass
            elif counter == 3:
                #3 extract description
                pass
            counter += 1
    

print('end script')
