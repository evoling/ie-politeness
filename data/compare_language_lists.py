#!/usr/bin/env python3
"""
Check the taxon lists in each of the raw data files:
    - tree file
    - pronoun paradigms
    - SAE features
    - metadata
"""

fix_tree_labels = {
        "Singhalese":"Sinhalese",
        "Welsh":"Welsh_N",
        "Serbian":"Serbocroatian",
        "Tosk":"Albanian_Tosk",
        "Luxembourgish":"Luxemburgish",
        "Belarusian":"Byelorussian",
        "Irish":"Irish_A",
        "Digor_Ossetic":"Iron_Ossetic",
        "Eastern_Armenian":"Armenian",
        "Arvanitika":"Albanian_Gheg", # proxy
        "Old_Church_Slavic":"Old_Church_Slavonic",
        "Cagliari":"Sardinian_Campidanese", # check
        "Nuorese":"Sardinian_Logudorese", # check
        "Old_West_Norse":"Old_Norse",
        "Bihari":"Maithili",
        }

tree_labels = set()
paradigm_labels = set()
sae_labels = set()
metadata_labels = set()

with open("pronoun-paradigms.csv") as fo:
    next(fo)
    for line in fo:
        paradigm_labels.add(line.split()[0])

with open("../analysis/ie-v1.mcc.tre") as fo:
    while next(fo).strip() != "Taxlabels":
        pass
    while True:
        label = next(fo).strip()
        if label != ";":
            try:
                label = fix_tree_labels[label]
            except KeyError:
                pass
            tree_labels.add(label)
        else:
            break

with open("../analysis/SAE-features-83.csv") as fo:
    next(fo)
    for line in fo:
        sae_labels.add(line.split()[0])

with open("../analysis/language-metadata.csv") as fo:
    next(fo)
    for line in fo:
        metadata_labels.add(line.split()[0])

shared_labels = paradigm_labels & tree_labels & sae_labels & metadata_labels
# print(*sorted(shared_labels), len(shared_labels))

unshared_labels = (paradigm_labels | tree_labels | sae_labels | metadata_labels).difference(shared_labels)
# print(*sorted(unshared_labels), len(unshared_labels))

for label in sorted(unshared_labels):
    row = [label]
    if label in metadata_labels:
        row.append("meta")
    if label in paradigm_labels:
        row.append("para")
    if label in tree_labels:
        row.append("tree")
    if label in sae_labels:
        row.append("sae ")
    print(*row)






