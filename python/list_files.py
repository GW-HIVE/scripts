import os
import csv
import glob

__version__ = "1.0"
__status__ = "Dev"
"""
This script will print(std out) all the fieldnames and field in the file path.
input: 
all the <filename.csv> under folder you set.
Usage:
python foramanraj.py
"""


###############################
def main():
    """sample"""
    pattern = "*.csv"
    file_path_list = glob.glob(pattern)

    seen = {}
    for file_path in file_path_list:
        file_names = os.path.basename(file_path)
        with open(file_path, 'r') as file_reader:
            data_frame = csv.reader(file_reader, delimiter=',', quotechar='"')
            row_count = 0
            for row in data_frame:
                row_count += 1
                if row_count == 1:
                    for field in row:
                        if field not in seen:
                            seen[field] = []
                        seen[field].append(file_names)

    for field in seen:
        file_names = seen[field]
        if len(file_names) > 1:
            for i in range(0, len(file_names)):
                for j in range(i, len(file_names)):
                    output = "%s.%s,%s.%s" % (file_names[i], field, file_names[j], field)
                    print(output)


if __name__ == '__main__':
    main()
