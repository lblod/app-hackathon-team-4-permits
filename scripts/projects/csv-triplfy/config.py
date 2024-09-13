from os.path import realpath, join
from os import makedirs



keys_lang = "nl" #en and nl

graph_name = "aanduidingsobjecten"
# graph_name = "aanduidingsobjecten_2K"
subject_uri = "https://inventaris.onroerenderfgoed.be/aanduidingsobjecten/"
subject_type = "http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object"

# graph_name = "erfgoedobjecten"
# subject_uri = "https://inventaris.onroerenderfgoed.be/erfgoedobjecten/"
# subject_type = "http://www.cidoc-crm.org/cidoc-crm/E22_Man-Made_Object"



# graph_name = "waarnemingen" #observations
# subject_uri = "https://inventaris.onroerenderfgoed.be/erfgoedobjecten/"
# subject_type = "http://www.cidoc-crm.org/cidoc-crm/E1_CRM_Entity"


# graph_name = "erfgoedobjecten_houtige_beplantingen_met_erfgoedwaarde" #observations


dataset_path = join(realpath('.'), 'data', f'{graph_name}.csv')
keys_path = join(realpath('.'), 'data', f'{graph_name}_keys.csv')
results_path = join(realpath('.'), 'results')
makedirs(results_path, exist_ok=True)

thes_path = join(realpath('.'), 'data', 'thesaurus', '20240912173420-thesaurus.ttl')


semantic_mapping_path = join(realpath('.'), 'data', 'semantic_mapping.csv')
