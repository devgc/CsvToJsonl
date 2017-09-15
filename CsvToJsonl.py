import argparse
import csv
import json

def GetOptions():
    usage = "CSV to JSONL"

    options = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=(usage)
    )

    options.add_argument(
        '-f',
        '--file',
        dest='csv_file',
        action="store",
        type=unicode,
        required=True,
        help='The csv file to transform'
    )
    
    options.add_argument(
        '-d',
        '--delimiter',
        dest='delimiter',
        action="store",
        type=str,
        required=True,
        help='The field delimiter'
    )

    return options

def main():
    options = GetOptions()
    options = options.parse_args()
    
    with open(options.csv_file,'rb') as filehandle:
        reader = csv.DictReader(filehandle,delimiter=options.delimiter)
        for row in reader:
            print json.dumps(row)
    

if __name__ == "__main__":
    main()