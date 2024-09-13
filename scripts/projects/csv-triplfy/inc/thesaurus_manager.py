from os.path import join, realpath
from rdflib import Graph



def load_thesaurus(thes_path):

    # Create a new RDF graph
    g = Graph()

    # Load the Turtle file into the graph (provide the path to your .ttl file)
    g.parse(thes_path, format="ttl")

    thes_dict = {}
    # Optionally, you can print the contents of the graph
    for subj, pred, obj in g:
        # print(f"Subject: {subj}, Predicate: {pred}, Object: {obj}")
        if 'prefLabel' in pred:
            thes_dict.update({str(obj).lower().replace(" ", ""): subj})
    return thes_dict