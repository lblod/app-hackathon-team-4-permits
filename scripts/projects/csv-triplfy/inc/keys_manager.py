from os import listdir
from os.path import join, realpath

import pandas as pd
from pandas import DataFrame

import config

def explore_original_keys(dataset_path):
    df = pd.read_csv(dataset_path, encoding="utf8", dtype='str', header=0)
    keys = df.columns.tolist()
    df_keys = DataFrame({"keys": keys})
    df_keys.to_csv(join(config.results_path, f"{config.graph_name}_keys.csv"))
    print(f"{config.graph_name} has : {len(df)} records described with {len(keys)} attributes")

def get_unique_keys():
    all_files_file_path = join(realpath('.'), 'data', 'keys')
    keys_files = listdir(all_files_file_path)
    keys_lst = []
    for kf in keys_files:
        df = pd.read_csv(join(all_files_file_path, kf), encoding="utf8", dtype='str', header=0)
        keys_lst.extend(df['keys'].tolist())

    # get unique keys i.e., those we look for semantic mapping for
    unique_keys = list(set(keys_lst))
    unique_keys.sort()
    print(f'From the {len(keys_files)} data sources, there are {len(unique_keys)} unique key')
    for k in unique_keys:
        print(k)

