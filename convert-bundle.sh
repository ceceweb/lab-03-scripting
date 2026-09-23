#!/bin/bash
set -euo pipefail

URL="https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz"
ARCHIVE="lab3-bundle.tar.gz"

curl -L -o "$ARCHIVE" "$URL"


tar -xzf "$ARCHIVE"


TSV=$(tar -tzf "$ARCHIVE" | grep '\.tsv$' | sed -n '1p')
echo "Found data file: $TSV"

awk '!/^[[:space:]]*$/' "$TSV" > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

ROWS=$(tail -n +2 cleaned.csv | wc -l | tr -d ' ')
echo "Data rows remaining: $ROWS"

tar -czf converted-archive.tar.gz cleaned.csv
