# Welcome to the GWU HIVE lab python scripts repository.
In this repository you will find useful resources related to the HIVE platfrom. For each script and folder, a breif introduction of their function and contents are listed as below. You can also click on each script to see for more details in the code documentation section.

## 1.[input_data](https://github.com/GW-HIVE/scripts/tree/main/io_data/input_data)
This folder includes all sample input files which could be used to test the python scripts.

## 2.[csv-parser.1.py](https://github.com/GW-HIVE/scripts/blob/main/python/csv-parser.1.py)
* Function: This script will transfer the .csv file to dataframe and print(std out) all the rows in the file with row number.
* Command line input: `python csv-parser.1.py -i <filename.csv>`
* Input file:	[A.csv]https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/A.csv)

## 3.[dump-csv-stats.py](https://github.com/GW-HIVE/scripts/blob/main/python/dump-csv-stats.py)
* Function: This script will print (std out) the fieldnames and the number of elements in each fieldname after spited by value.
* Command line input: `python dump-csv-stats.py -i <filename.csv> -d value`
* Input file:	[A.csv](https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/A.csv)

## 4.[dump-fasta-stats.py](https://github.com/GW-HIVE/scripts/blob/main/python/dump-fasta-stats.py)
* Function: This script will check the .fasta file that if there are duplicate IDs in the sequence.
* Command line input: `python dump-fasta-stats.py -i <filename.fasta>`
* Input file:	[sample.fasta](https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/sample.fasta)

## 5.[fasta-parser.py](https://github.com/GW-HIVE/scripts/blob/main/python/fasta-parser.py)
* Function: This script will print (std out) the sequence of a record with id equals "ENST00000357654".
* Command line input: `python fasta-parser.py -i <filename.fasta>`
* Input file:	[sample.fasta](https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/sample.fasta)

## 6.[fastq-parser.py](https://github.com/GW-HIVE/scripts/blob/main/python/fastq-parser.py)
* Function: This script will print (std out) the read_id, read_seq and read_qual from the input fastq file.
* Command line input: `python fastq-parser.py -i <filename.fastq>`
* Input file:	[1G_data.fastq](https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/1G_data.fastq)


## 7.[foramanraj.1.py](https://github.com/GW-HIVE/scripts/blob/main/python/foramanraj.1.py)
* Function: This script will print(std out) all the fieldnames and field in the file path.
* Command line input: `python foramanraj.py`
* Input file:	No input files are required.

## 8.[parse-big-fasta.py](https://github.com/GW-HIVE/scripts/blob/main/python/parse-big-fasta.py)
* Function: This script was designed to parse the RVDB formatted FASTA headers so they can be interperated by HIVE-hexagon's tablequery
* Command line input: `python parse-big-fasta.py -i <filename.fastq>`
* Input file: N/A


## 9.[parse-csv.py](https://github.com/GW-HIVE/p/parse-csv.py)
* Function: This script will print(std out) an array. This array contains the original csv file and add a column at last. Elements in the new last column is the product of the third row and the fourth row, and it will ignore the first row(because it is normally titles for the rows)
* Command line input: `python parse-csv.py`
* Input file:	No input files are required.

## 10.[sas7bdatTocsv.1.py](https://github.com/GW-HIVE/scripts/blob/main/python/sas7bdatTocsv.1.py)
* Function: This script will transfer a .sas7bdat file to a .csv file.
* Command line input: `python sas7bdatTocsv.1.py -i <input.sas7bdat> -o <output.csv>`
* Input file:[gold.sas7bdat](https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/gold.sas7bdat)

## 11.[sas7bdatTocsv.2.py](https://github.com/GW-HIVE/scripts/blob/main/python/sas7bdatTocsv.2.py)
* Function: This script will transfer the .sas7bdat file to .csv format and print(std out) each line of the file(replace all the "," with ":" in each row).
* Command line input: `python sas7bdatTocsv.2.py -i <filename.sas7bdat>`
* Input file:[gold.sas7bdat](https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/gold.sas7bdat)

## 12.[toy.py](https://github.com/GW-HIVE/scripts/blob/main/python/toy.py)
* Function: This script will print(std out) all the rows with row number in a .csv file.
* Command line input: `python parse-csv.py`
* Input file:	No input files are required.


## 13.[xml-parser.1.py](https://github.com/GW-HIVE/scripts/blob/main/python/xml-parser.1.py)
* Function:	This script will print(std out) some domains of a .xml file.
* Command line input: `python xml-parser.1.py -i <filename.xml>`
* Input file:[sample.xml](https://github.com/GW-HIVE/scripts/blob/main/io_data/input_data/sample.xml)

## 14.[quote_csv.py](https://github.com/GW-HIVE/scripts/blob/main/python/quote_csv.py)
* Function:	This script will add double quotes to all values in a csv file. If a value is already quoted, quotes will not be added to that value. If there is quoted text within a value the quoted text will now have two sets of quotes e.g. ""quoted text"".
* Command line input: `python quote_csv.py -f input.csv -o output.csv`
* Input file: any csv file.

## 15.[outFile](https://github.com/GW-HIVE/scripts/blob/main/io_data/outFile)
* This is a sample output file.

## 16.[VCFReformatter.py](https://github.com/GW-HIVE/scripts/blob/main/python/VCFReformatter.py)
* Function: This script will convert a VCF file generated by HIVE Heptagon into the [VCF standard](https://samtools.github.io/hts-specs/VCFv4.2.pdf) (PDF) to be compatible with other applications. Uses [csv](https://github.com/python/cpython/blob/3.9/Lib/csv.py) and [re](https://github.com/python/cpython/blob/3.9/Lib/re.py) modules.
* Command line input: NA (written in an IDE, so input file is hard coded (on line 29). Would have to be rewritten for command line args if meant to be executed at CLI).
* Intput file: a .vcf file generated by HIVE Heptagon.

## 17.Tips
* If you see "ImportError: No module named xxx" when you execute the script, just do "pip install xxx" and execute the script again.
* All the python scripts are modified to be executed by Python3, if you meet problem arising from python version, please contact us at once.









