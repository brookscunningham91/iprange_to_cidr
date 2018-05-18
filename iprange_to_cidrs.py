"""
example

python iprange_to_cidr.py --incsv somefile.csv

"""

from netaddr import iprange_to_cidrs
import csv
import argparse

parser = argparse.ArgumentParser(description='Bulk stuff')
parser.add_argument('--incsv', help='Specify the csv file with the list of ip ranges', required=True, default=False)
args = parser.parse_args()


def get_cidrs(file_location):
    list_of_cidrs = []
    with open(file_location, 'rt') as csvfile:
        ip_start_and_end = csv.reader(csvfile, delimiter=',')
        for row in ip_start_and_end:
            list_of_cidrs.append(iprange_to_cidrs(row[0], row[1]))

        return list_of_cidrs

cidrs_array = get_cidrs(args.incsv)
for ipcidrs in cidrs_array:
    if len(ipcidrs) > 0 :
        for cidr in ipcidrs:
            print(cidr)
    else:
        print(ipcidrs)

