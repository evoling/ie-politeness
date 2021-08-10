#!/usr/bin/env python3
"""
This script was used to transform the pronoun-paradigms.csv table into pronoun-number-conflation.csv::

    python make_pronoun_conflation_table.py > pronoun-number-conflation.csv

The output file has already been stored in this repository, and it it not necessary to run this script again.
"""
import csv

FILENAME = "pronoun-paradigms.csv"

def get_values(D, start_str):
    for key, value in D.items():
        if key.startswith(start_str):
            for lex in value.split(","):
                lex = lex.lower().strip()
                if lex:
                    yield lex
    return

print("language", "conflation", sep="\t")
with open(FILENAME) as fileobj:
    reader = csv.DictReader(fileobj, delimiter="\t")
    for row in reader:
        forms_2sg = {f for f in get_values(row, "2sg")}
        forms_2pl = {f for f in get_values(row, "2pl")}
        forms_3sg = {f for f in get_values(row, "3sg")}
        forms_3pl = {f for f in get_values(row, "3pl")}
        print(row["language"], 
                1 if (forms_2sg & forms_2pl) or bool(forms_3sg &
                forms_3pl) else 0, sep="\t")
        #print(forms_2sg, forms_2pl, forms_3sg, forms_3pl)
