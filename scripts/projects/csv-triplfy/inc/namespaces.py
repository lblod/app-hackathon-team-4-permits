from rdflib import Namespace, Graph
from rdflib.namespace import RDFS
from rdflib.namespace import XSD
import rdflib

import config

# one shared URI and prefix for all classes and relations of BMO


# Vocab reuse sources
namespaces_dict = {
    "onr": Namespace(config.subject_uri),
    "app": Namespace("http://app.hackathon-4.s.redhost.be/"),

    'sdo': Namespace("https://schema.org/"),
    'dct': Namespace("http://purl.org/dc/terms/"),
    'aat': Namespace("http://vocab.getty.edu/aat/"),
    'tgn': Namespace("http://vocab.getty.edu/tgn/"),
    'ulan': Namespace("http://vocab.getty.edu/ulan/"),
    'cidoc': Namespace("http://www.cidoc-crm.org/crm/"),
    'edm': Namespace("http://www.europeana.eu/schemas/edm/"),
    'time': Namespace("http://www.w3.org/2006/time#"),
    'dcmi': Namespace("http://dublincore.org/documents/dcmi-terms/#")

}

# onto = rdflib.URIRef(namespaces_dict["app"].ontology)


def bind_namespace(g):
    # retrieve namespace manager from the graph
    nm = g.namespace_manager

    # bind it to the namespace manager
    for k, v in namespaces_dict.items():
        nm.bind(k, v)
