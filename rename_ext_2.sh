#!bin/bash
for f in *.docx; do
    mv -- "$f" "${f%.docx}".txt
done