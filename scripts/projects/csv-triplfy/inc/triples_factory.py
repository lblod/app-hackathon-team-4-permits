from os.path import join

import pandas as pd
from pandas import DataFrame
from rdflib import RDF, Literal, URIRef

import config
from inc import namespaces




def load_keys(keys_path):
    df = pd.read_csv(keys_path, encoding="utf8", header=0, dtype='str')
    df.replace(to_replace=" ", value="_", regex=True, inplace=True)
    return df[config.keys_lang]


def load_csv(dataset_path, keys):
    df = pd.read_csv(dataset_path, encoding="utf8", dtype='str', names=keys, header=0)

    df.fillna("", inplace=True)

    df.replace(to_replace="Onbepaald", value="", inplace=True)

    df.astype("str")

    return df


def get_triples(dataset_path, keys_path, thes_dict):
    keys = load_keys(keys_path)

    df = load_csv(dataset_path, keys)

    triples = []
    for i, row in df.iterrows():
        s = row["id"]
        triples.append([s, 'instance', URIRef(config.subject_type)])
        for p in keys[1:]:
            o = row[p]

            if 'type' in p:
                # We should look inside the thesaurus about the corresponding ID
                o = thes_dict.get(o.lower().replace(" ", ""), Literal(o))
                triples.append([s, p, o])
                continue

            # skipping empty objects
            if o != "":
                os = o.split(',')
                for oi in os:
                    triples.append([s, p, Literal(oi)])

    print(len(triples))
    return triples
