import sys
import os.path
import csv
import pandas as pd

def main():
    # Define the base URL for the MGI API
    base_dir = os.path.abspath(os.path.dirname(__file__))

    DBDIR = os.path.join(base_dir,  'databases')
    mouse_genesInfo_filepath = os.path.join(DBDIR, 'MRK_List2.rpt')
    human_genesInfo_filepath = os.path.join(DBDIR, 'trrust_rawdata.human.tsv')

    mouse_genesInfo = pd.read_csv(mouse_genesInfo_filepath, sep='\t')
    human_genesInfo = pd.read_csv(human_genesInfo_filepath, sep='\t', header= None, dtype = str)

    mouse_symbols = (mouse_genesInfo.loc[:,'Marker Symbol'])
    human_symbols = human_genesInfo.loc[:,1]
    #print(human_symbols)

    if len(sys.argv) == 1:
        print("No gene listed")
    else:
        geneSymbol = sys.argv[1] 

        if geneSymbol in mouse_symbols.values:
            resultStr = "Valid Mouse Gene"
        elif geneSymbol in human_symbols.values:
            resultStr = "Valid Human Gene"
        else:
            resultStr = "Not a mouse or human gene"




        if len(sys.argv) > 2:
            size = sys.argv[2] + " size network"
        else:
            size = "reduced size network"

        filename = "results.csv"
        data = [resultStr,size]
        with open(filename, 'w+', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Write data to the CSV file row by row
            for row in data:
                csvwriter.writerow([row])

if __name__ == '__main__':
    exit(main())
