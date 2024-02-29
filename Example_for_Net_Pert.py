import sys
import os.path
import csv
import pandas as pd

# Define the base URL for the MGI API

DBDIR = os.path.join( 'databases')
mouse_genesInfo_filepath = os.path.join(DBDIR, 'MRK_List2.rpt')
human_genesInfo_filepath = os.path.join(DBDIR, 'trrust_rawdata.human.tsv')

mouse_genesInfo = pd.read_csv(mouse_genesInfo_filepath, sep='\t')
human_genesInfo = pd.read_csv(human_genesInfo_filepath, sep='\t', header= None, dtype = str)

mouse_symbols = (mouse_genesInfo.loc[:,'Marker Symbol'])
human_symbols = human_genesInfo.loc[:,1]
#print(human_symbols)
geneSymbol = sys.argv[1] 

if geneSymbol in mouse_symbols.values:
    resultStr = "Valid Mouse Gene"
elif geneSymbol in human_symbols.values:
    resultStr = "Valid Human Gene"
else:
    resultStr = "Not a mouse or human gene"





size = sys.argv[2] + " size network"

filename = "results.csv"
data = [resultStr,size]
with open(filename, 'w+', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

        # Write data to the CSV file row by row
    for row in data:
        csvwriter.writerow([row])
