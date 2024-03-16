#!/usr/bin/env bash

# Function to download a file and handle errors
download_file() {
    local url="$1"
    local file_name="$2"

    echo "Downloading $file_name from $url"
    if curl -fsSL "$url" -o "$file_name"; then
        echo "Download successful: $file_name"
    else
        echo "Error: Failed to download $file_name from $url"
        exit 1
    fi
}

# Change directory to the 'databases' directory
cd "$(dirname "$0")/databases" || exit 1

# Download files
download_file "https://www.informatics.jax.org/downloads/reports/MRK_List2.rpt" "MRK_List2.rpt"
download_file "https://www.grnpedia.org/trrust/data/trrust_rawdata.human.tsv" "trrust_rawdata.human.tsv"

