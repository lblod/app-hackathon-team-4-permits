from os.path import join

import pandas as pd
import rdflib
from rdflib import Graph, Literal, SKOS, XSD, RDF, URIRef
from inc import namespaces, triples_factory, keys_manager, thesaurus_manager

import config, meta_config
from inc.namespaces import namespaces_dict


def load_semantic_mapping():
    df = pd.read_csv(config.semantic_mapping_path, encoding="utf8", header=0)
    semantic_mapping = {}
    for i, row in df.iterrows():
        semantic_mapping.update({row['nl']: row['mapping']})

    return semantic_mapping


def get_predicate_uri(p, semantic_mapping):
    # I think we should look back to the semantic mapping file or where the keys are
    uri = URIRef(semantic_mapping.get(p, '{}{}'.format(namespaces_dict["app"], p)))

    if 'aat' in uri:
        uri = URIRef('{}{}'.format(namespaces_dict['aat'], p))

    if 'tgn' in uri:
        uri = URIRef('{}{}'.format(namespaces_dict['tgn'], p))

    if 'instance' in p:
        uri = RDF.type
    return uri


def add_triples(g, triples, semantic_mapping):
    for triple in triples:
        s, p, o = triple
        s = URIRef('{}{}'.format(namespaces_dict["onr"], s))
        p = get_predicate_uri(p, semantic_mapping)
        #o = Literal('{}'.format(o))
        if o is None:
            print('here')
        g.add((s, p, o))


# def add_schema_metadata(g):
#     """
#     Add corresponding metadata from the meta_config file to the created schema
#     """
#     g.add((onto, RDF.type, SKOS.ConceptScheme))
#     g.add((onto, dct.title, Literal(meta_config.schema_title, lang="en")))
#     g.add((onto, dct.description, Literal(meta_config.schema_description, lang="en")))
#     g.add((onto, dct.license, Literal(meta_config.license_url)))
#     g.add((onto, dct.created, Literal(meta_config.created_at, datatype=XSD.date)))
#     creator = rdflib.BNode()
#     g.add((creator, sdo.name, Literal(meta_config.author)))
#     g.add((creator, sdo.identifier, Literal(meta_config.orcid)))
#     affiliation = rdflib.BNode()
#     g.add((affiliation, sdo.name,
#            Literal(meta_config.institute)))
#     g.add((affiliation, sdo.url, Literal(meta_config.institute_url)))
#     g.add((creator, sdo.affiliation, affiliation))
#     g.add((onto, dct.creator, creator))


def explore():
    # keys_manager.explore_original_keys(config.dataset_path)
    keys_manager.get_unique_keys()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # explore()

    thes_dict = thesaurus_manager.load_thesaurus(config.thes_path)

    triples = triples_factory.get_triples(config.dataset_path, config.keys_path, thes_dict)

    # init empty graph
    g = Graph()

    # bind the name spaces
    namespaces.bind_namespace(g)

    # add schema metadata
    # add_schema_metadata(g)

    # load semantic_mapping
    semantic_mapping = load_semantic_mapping()

    # add actual triples
    add_triples(g, triples, semantic_mapping)

    # exports to three formats Turtle, RDF and n-triples.
    g.serialize(destination=join(config.results_path, f"{config.graph_name}.ttl"), format="ttl", encoding="utf-8")
    g.serialize(destination=join(config.results_path, f"{config.graph_name}.rdf"), format="pretty-xml",
                encoding="utf-8")
