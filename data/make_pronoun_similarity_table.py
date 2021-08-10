#!/usr/bin/env python3
"""
Convert a paradigm into a similarity table

Paradigm:
        ... 2sg 2pl 3sgM ...
English ... you you   he ...
Swedish ...  du  ni  han ...

Similarity:
        ... 2sg.2pl 2sg.3sgM 2pl.3sgM  ...
English ...       1        0        0  ...
Swedish ...       0        0        0  ...

Where there a multiple forms in a paradigm cell a match with any counts as 1 in the similarity comparison.

Usage::

    python make_pronoun_similarity_table.py > pronoun-similarity.csv

The output file has already been stored in this repository, and it it not necessary to run this script again.
"""
import csv

FILENAME = "pronoun-paradigms.csv"

def set_split(s):
    return {item.strip() for item in s.split(",")}

pairs = None
metadata = {"language", "iso_code"}
with open(FILENAME) as fileobj:
    reader = csv.DictReader(fileobj, delimiter="\t")
    for row in reader:
        output = []
        output.append(row["language"])
        if not pairs:
            pairs = [(i, j) for i in row.keys() for j in row.keys()
                    if i < j and i not in metadata and j not in metadata]
            print("language", *["{}.{}".format(*p) for p in pairs], sep="\t")
        for i, j in pairs:
            output.append(1 if set_split(row[i]) & set_split(row[j]) else 0)
        print(*output, sep="\t")
            
