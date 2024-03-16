#!/usr/bin/env bash

cd "$(dirname "$0")/databases"

curl -O https://www.informatics.jax.org/downloads/reports/MRK_List2.rpt

curl -O -k https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv
