#!/usr/bin/env python3
"""
This script was used to transform the pronoun-paradigms.csv table into
pronoun-distinct-politeness.csv, which shows whether languages have overlap
between their polite and intimate forms in 2sg or 2pl::

    python make_distinct_politeness_table.py > pronoun-distinct-politeness.csv

The output file has already been stored in this repository, and it it not
necessary to run this script again.
"""
import csv

FILENAME = "pronoun-paradigms.csv"

print("language", "distinct", sep="\t")
with open(FILENAME) as fileobj:
    reader = csv.DictReader(fileobj, delimiter="\t")
    for row in reader:
        forms_2sg = set(row["2sg"].strip().split(","))
        forms_2sg_polite = set(row["2sgsuperform"].strip().split(","))
        forms_2pl_m = set(row["2plmasc"].strip().split(","))
        forms_2pl_f = set(row["2plfem"].strip().split(","))
        forms_2pl_polite = set(row["2plsuperform"].strip().split(","))
        print(row["language"], 
                0 if (forms_2sg_polite & forms_2sg) or 
                (forms_2pl_polite & (forms_2pl_m | forms_2pl_f))
                else 1, sep="\t")
