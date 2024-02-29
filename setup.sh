#!/usr/bin/env bash
source ~/.venv/bin/activate
cd ./databases

curl -O https://www.informatics.jax.org/downloads/reports/MRK_List2.rpt

curl -O -k https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv
